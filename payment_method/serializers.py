from rest_framework import serializers
from .models import PaymentMethod
from services.validations import validate_unique


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ["id", "name", "status"]


validation = validate_unique()


class PaymentMethodCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    status = serializers.BooleanField(read_only=True)

    def validate(self, attrs):
        validate_unique.name(PaymentMethod, attrs)
        return attrs

    def create(self, validated_data):
        return PaymentMethod.objects.create(**validated_data)


class PaymentMethodUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    status = serializers.BooleanField(read_only=True)

    def validate(self, attrs):
        validate_unique.name(PaymentMethod, attrs, self.instance)
        return attrs

    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()
        validated_data["message"] = f"Método de pago {instance.name} actualizada !"
        return validated_data
