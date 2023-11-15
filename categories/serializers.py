from rest_framework import serializers
from .models import Category
from services.validations import validate_unique


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "status"]


validation = validate_unique()


class CategorieCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    status = serializers.BooleanField(read_only=True)

    def validate(self, attrs):
        validate_unique.name(Category, attrs)
        return attrs

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class CategorieUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    status = serializers.BooleanField(read_only=True)

    def validate(self, attrs):
        validate_unique.name(Category, attrs, self.instance)
        return attrs

    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()
        validated_data["message"] = f"Categoria {instance.name} actualizada !"
        return validated_data
