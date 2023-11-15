from .models import ItemShopCart
from rest_framework import serializers
from products.models import Product
from services.validations import validate_stock


class ItemShopCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemShopCart
        fields = ["id", "product", "quantity"]


validation = validate_stock()


class ItemShopCartCreateSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(status=True).order_by("name")
    )
    quantity = serializers.IntegerField()

    def validate(self, attrs):
        validate_stock.quantity(attrs)
        return attrs

    def create(self, validated_data):
        return ItemShopCart.objects.create(**validated_data)


class ItemShopUpdateSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(status=True).order_by("name")
    )
    quantity = serializers.IntegerField()

    def validate(self, attrs):
        validate_stock.quantity(attrs)
        return attrs

    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()
        validated_data["message"] = f"Producto {instance.name} actualizado !"
        return validated_data
