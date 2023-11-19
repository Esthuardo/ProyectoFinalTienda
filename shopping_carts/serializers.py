from rest_framework import serializers
from .models import Shopping_cart
from clients.models import Client
from itemsShopCart.models import ItemShopCart
from payment_method.models import PaymentMethod
from services.validations import validate_field
from datetime import datetime


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping_cart
        fields = [
            "id",
            "client",
            "items",
            "date",
            "payment_method",
            "direction",
            "total",
        ]


class ShoppingCartCreateSerializer(serializers.Serializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.filter(status=True)
    )
    items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ItemShopCart.objects.all()
    )
    payment_method = serializers.PrimaryKeyRelatedField(
        queryset=PaymentMethod.objects.filter(status=True)
    )
    direction = serializers.CharField()

    def validate(self, attrs):
        # validate_field.status(Client, "id", attrs)
        return attrs

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        shopping_cart = Shopping_cart.objects.create(**validated_data)
        shopping_cart.items.set(items_data)
        return shopping_cart

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["id"] = instance.id
        return rep


class ShoppingCartUpdateSerializer(serializers.Serializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ItemShopCart.objects.all(), required=False
    )
    payment_method = serializers.PrimaryKeyRelatedField(
        queryset=PaymentMethod.objects.filter(status=True), required=False
    )
    total = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    direction = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items", None)
        if items_data is not None:
            instance.items.set(items_data)
        for attr, value in validated_data.items():
            if attr != "date":
                setattr(instance, attr, value)
        instance.date = datetime.now()
        instance.save()
        return instance
