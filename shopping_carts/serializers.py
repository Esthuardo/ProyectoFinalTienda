from rest_framework import serializers
from .models import Shopping_cart
from clients.serializers import ClientSerializer
from clients.models import Client
from itemsShopCart.serializers import ItemShopCartSerializer
from itemsShopCart.models import ItemShopCart
from payment_method.serializers import PaymentMethodSerializer
from payment_method.models import PaymentMethod
from services.validations import validate_field


class ShoppingCartSerializer(serializers.ModelSerializer):
    # client = ClientSerializer(read_only=True)
    # items = ItemShopCartSerializer(many=True, read_only=True)
    # payment_method = PaymentMethodSerializer(read_only=True)

    class Meta:
        model = Shopping_cart
        fields = ["client", "items", "date", "payment_method", "direction"]


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
        return Shopping_cart.objects.create(**validated_data)
