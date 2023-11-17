from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed, NotFound
from rest_framework_simplejwt.tokens import RefreshToken
from secrets import token_hex
from users.serializers import UserCreateSerializer


class RegisterSerializer(serializers.Serializer):
    user = UserCreateSerializer()
    password_confirmation = serializers.CharField(max_length=12, write_only=True)

    def validate_password_confirmation(self, value):
        data = self.get_initial()
        if "user" in data and "password" in data["user"]:
            if value != data["user"]["password"]:
                raise serializers.ValidationError("Password dont match")
        return value

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        return User.objects.create_user(**user_data)

    def to_representation(self, instance):
        # Utiliza UserCreateSerializer para serializar la instancia de User
        return UserCreateSerializer(instance).data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=50, write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=12, write_only=True)
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        username = obj.get("username")
        email = obj.get("email")
        password = obj.get("password")
        user = authenticate(username=username, password=password, email=email)
        jwt = RefreshToken.for_user(user)
        return {"access_token": str(jwt.access_token), "refresh_token": str(jwt)}

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        email = attrs.get("email")
        # validar que el usuario exista
        # validar que la contraseña sea correcta para el usuario
        if not authenticate(username=username, password=password, email=email):
            raise AuthenticationFailed("User not found or credentials is invalid")
        return attrs
