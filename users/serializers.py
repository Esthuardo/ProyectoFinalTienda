from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password", "username"]


def validate_unique_email(attrs, instance=None):
    email = attrs.get("email")
    if (
        User.objects.filter(email=email)
        .exclude(pk=instance.pk if instance else None)
        .exists()
    ):
        # Este if es más que nada al momento de actualizar que permita dejar el mismo correo
        raise serializers.ValidationError("El correo que quiere utilizar ya existe")
    return attrs


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate(self, attrs):
        validate_unique_email(attrs)
        return attrs


class UserUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()

    message = serializers.ReadOnlyField()

    def validate(self, attrs):
        validate_unique_email(attrs)
        return attrs

    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()
        validated_data["message"] = f"Usuario {instance.first_name} actualizado !"
        return validated_data
