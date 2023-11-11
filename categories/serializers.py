from rest_framework import serializers
from .models import Category


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "status"]


def validate_unique_categorie(attrs, instance=None):
    name = attrs.get("name")
    if name:
        categorie = Category.objects.filter(name=name)
        if instance != None:
            categorie = categorie.exclude(pk=instance.pk)
        if categorie.exists():
            raise serializers.ValidationError(f"La categoria {name} ya existe")
    return attrs


class CategorieCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)

    def validate(self, attrs):
        validate_unique_categorie(attrs)
        return attrs

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class CategorieUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)

    def validate(self, attrs):
        validate_unique_categorie(attrs, self.instance)
        return attrs

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
