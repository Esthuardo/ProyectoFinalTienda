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
        fields = ["client", "items", "date", "payment_method", "direction", "total"]


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

    def validate(self, attrs):
        # validate_field.status(Client, "id", attrs)
        return attrs

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        shopping_cart = Shopping_cart.objects.create(**validated_data)
        shopping_cart.items.set(items_data)
        return shopping_cart


class ShoppingCartUpdateSerializer(serializers.Serializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ItemShopCart.objects.all()
    )
    payment_method = serializers.PrimaryKeyRelatedField(
        queryset=PaymentMethod.objects.filter(status=True)
    )
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    direction = serializers.CharField()

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items")
        for attr, value in validated_data.items():
            if attr != "date":
                setattr(instance, attr, value)
        instance.date = datetime.now()
        instance.items.set(items_data)
        instance.save()
        return instance
