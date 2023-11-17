from rest_framework import serializers
from clients.models import Client
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed, NotFound
from rest_framework_simplejwt.tokens import RefreshToken
from clients.serializers import ClientCreateSerializer
from .permissions import authenticate_client


class RegisterClientSerializer(serializers.Serializer):
    client = ClientCreateSerializer()
    password_confirmation = serializers.CharField(max_length=12, write_only=True)

    def validate_password_confirmation(self, value):
        data = self.get_initial()
        if "client" in data and "password" in data["client"]:
            if value != data["client"]["password"]:
                raise serializers.ValidationError("Password dont match")
        return value

    def create(self, validated_data):
        client_data = validated_data.pop("client")
        return Client.objects.create(**client_data)

    def to_representation(self, instance):
        # Utiliza UserCreateSerializer para serializar la instancia de User
        return ClientCreateSerializer(instance).data


class LoginClientSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=12, write_only=True)
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        email = obj.get("email")
        password = obj.get("password")
        client = authenticate_client(email=email, password=password)
        jwt = RefreshToken.for_user(client)
        return {"access_token": str(jwt.access_token), "refresh_token": str(jwt)}

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if not authenticate_client(email=email, password=password):
            raise AuthenticationFailed("Client not found or credentials is invalid")
        return attrs
