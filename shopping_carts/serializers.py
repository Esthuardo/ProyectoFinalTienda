from rest_framework import serializers
from .models import Shopping_cart
from clients.serializers import ClientSerializer
from itemsShopCart.serializers import ItemShopCartSerializer


class ShoppingCartSerializer(serializers.ModelSerializer):
    items = ItemShopCartSerializer(many=True, read_only=True)

    class Meta:
        model = Shopping_cart
        fields = ["client", "items", "date", "payment_method", "direction"]
