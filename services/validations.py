from rest_framework import serializers


class validate_unique:
    # Validar que sea un email unico
    def email(table, attrs, instance=None):
        email = attrs.get("email")
        if email:
            user = table.objects.filter(email=email)
            if instance != None:
                user = user.exclude(pk=instance.pk)
            if user.exists():
                raise serializers.ValidationError(
                    "El correo que quiere utilizar ya existe"
                )
        return attrs

    # Validar que sea un codigo de barras y de aduanas unico
    def barcode_customsCode(table, attrs, instance=None):
        barcode = attrs.get("barcode")
        customs_code = attrs.get("customs_code")
        # Garantizamos que exista el codigo de barras y de aduanas
        if not all([barcode, customs_code]):
            raise serializers.ValidationError(
                "El código de aduanas y/o el código de barras no pueden estar vacíos."
            )
        # En caso de actualizar excluimos al propio producto en caso no se altere su codigo codigo de barras o aduanas
        product_exist = table.objects.exclude(pk=instance.id if instance else None)
        # Verificamos si existe
        if product_exist.filter(barcode=barcode).exists():
            raise serializers.ValidationError("Este código de barras ya está en uso.")
        if product_exist.filter(customs_code=customs_code).exists():
            raise serializers.ValidationError("Este código de aduanas ya está en uso.")

        return attrs

    # Validar que sea un nombre único
    def name(table, attrs, instance=None):
        name = attrs.get("name")
        if name:
            categorie = table.objects.filter(name=name)
            if instance != None:
                categorie = categorie.exclude(pk=instance.pk)
            if categorie.exists():
                raise serializers.ValidationError(f"La categoria {name} ya existe")
        return attrs


class validate_field:
    def quantity(attrs):
        print(attrs)
        product = attrs.get("product")
        stock = product.stock
        quantity = attrs.get("quantity")
        if quantity > stock:
            raise serializers.ValidationError(
                "La cantidad que intenta agregar es mayor al stock"
            )
        return attrs

    def status(table, field, attrs):
        search_field = attrs.get(field)
        filter_kwargs = {field: search_field, "status": True}
        if not table.objects.filter(**filter_kwargs).exists():
            raise serializers.ValidationError("Error al verificar si esta habilitado")
        return attrs


class ReactivateSerializer(serializers.Serializer):
    message = message = serializers.ReadOnlyField()
