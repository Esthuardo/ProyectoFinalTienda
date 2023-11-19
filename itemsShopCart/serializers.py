from .models import ItemShopCart
from rest_framework import serializers
from products.models import Product
from services.validations import validate_field


class ItemShopCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemShopCart
        fields = ["id", "product", "quantity"]


validation = validate_field()


class ItemShopCartCreateSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(status=True).order_by("name")
    )
    quantity = serializers.IntegerField()

    def validate(self, attrs):
        validate_field.quantity(attrs)
        return attrs

    def create(self, validated_data):
        return ItemShopCart.objects.create(**validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["id"] = instance.id
        return rep


class ItemShopUpdateSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()
        return validated_data
