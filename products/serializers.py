from rest_framework import serializers
from .models import Product
from categories.models import Category
from services.validateUnique import validate_unique


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "barcode",
            "customs_code",
            "description",
            "image",
            "number_order",
            "price",
            "stock",
            "status",
        ]


class ProductsCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(status=True).order_by("name"),
    )
    barcode = serializers.CharField(max_length=20)
    customs_code = serializers.CharField(max_length=30)
    description = serializers.CharField(style={"base_template": "textarea.html"})
    image = serializers.CharField()
    number_order = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=7, decimal_places=2)
    stock = serializers.IntegerField()
    status = serializers.BooleanField(read_only=True)

    def validate(self, attrs):
        validate_unique.barcode_customsCode(Product, attrs)
        return attrs

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class ProductsUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(status=True)
    )
    barcode = serializers.CharField(max_length=20)
    customs_code = serializers.CharField(max_length=30)
    description = serializers.CharField(style={"base_template": "textarea.html"})
    image = serializers.CharField(help_text="Ingresa el URL de la imagen")
    number_order = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=7, decimal_places=2)
    stock = serializers.IntegerField()
    status = serializers.BooleanField(read_only=True)

    def validate(self, attrs):
        validate_unique.barcode_customsCode(Product, attrs, self.instance)
        return attrs

    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()
        validated_data["message"] = f"Producto {instance.name} actualizado !"
        return validated_data


class ProductsSearchByNameSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
