from rest_framework import serializers
from .models import Product
from categories.models import Category


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


def validate_unique_barcode_customsCode(attrs, instance=None):
    barcode = attrs.get("barcode")
    customs_code = attrs.get("customs_code")
    # Garantizamos que exista el codigo de barras y de aduanas
    if not all([barcode, customs_code]):
        raise serializers.ValidationError(
            "El código de aduanas y/o el código de barras no pueden estar vacíos."
        )
    # En caso de actualizar excluimos al propio producto en caso no se altere su codigo codigo de barras o aduanas
    product_exist = Product.objects.exclude(pk=instance.id if instance else None)
    # Verificamos si existe
    if product_exist.filter(barcode=barcode).exists():
        raise serializers.ValidationError("Este código de barras ya está en uso.")
    if product_exist.filter(customs_code=customs_code).exists():
        raise serializers.ValidationError("Este código de aduanas ya está en uso.")

    return attrs


class ProductsCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(status=True)
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
        validate_unique_barcode_customsCode(attrs)
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
        validate_unique_barcode_customsCode(attrs, self.instance)
        return attrs

    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()
        validated_data["message"] = f"Producto {instance.name} actualizado !"
        return validated_data


class ProductsReactivateSerializer(serializers.Serializer):
    pass


class ProductsSearchByNameSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
