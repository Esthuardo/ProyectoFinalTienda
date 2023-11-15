from rest_framework import serializers
from .models import User
from services.validations import validate_unique


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password", "username"]


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate(self, attrs):
        validate_unique.email(User, attrs)
        return attrs


class UserUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50, required=False, write_only=True)
    email = serializers.EmailField(required=False, write_only=True)

    message = serializers.ReadOnlyField()

    def validate(self, attrs):
        validate_unique.email(User, attrs, self.instance)
        return attrs

    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()
        validated_data["message"] = f"Usuario {instance.first_name} actualizado !"
        return validated_data
