from rest_framework import serializers
from .models import Client
from services.validations import validate_unique


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "name",
            "surname",
            "email",
            "password",
            "phone_number",
            "direction",
            "status",
        ]


validation = validate_unique()


class ClientCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    surname = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=18)
    direction = serializers.CharField()
    status = serializers.BooleanField(read_only=True)

    # obviamos la validación de confirmar contraseña 2 veces por que eso ya se hace en el front-end
    def validate(self, attrs):
        validate_unique.email(Client, attrs)
        return attrs

    def create(self, validated_data):
        return Client.objects.create(**validated_data)


class ClientUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    surname = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=18)
    direction = serializers.CharField()

    # obviamos la validación de confirmar contraseña 2 veces por que eso ya se hace en el front-end
    def validate(self, attrs):
        validate_unique.email(Client, attrs, self.instance)
        return attrs

    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()
        validated_data["message"] = f"Cliente {instance.name} actualizado !"
        return validated_data
