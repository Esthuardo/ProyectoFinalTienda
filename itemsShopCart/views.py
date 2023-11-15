from .models import ItemShopCart
from .serializers import (
    ItemShopCartSerializer,
    ItemShopCartCreateSerializer,
    ItemShopUpdateSerializer,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import generics
from rest_framework.exceptions import NotFound

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


class ItemShopView(generics.GenericAPIView):
    serializer_class = ItemShopCartSerializer
    queryset = ItemShopCart.objects.all()
    http_method_names = ["get", "post"]

    @swagger_auto_schema(
        operation_summary="Endpoint para listar todos los productos en carrito",
        operation_description="Retoma una lista de productos",
    )
    def get(self, request):
        record = ItemShopCart.objects.all().order_by("product")
        serializer = self.get_serializer(record, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para crear un producto",
        operation_description="Crea un nuevo producto que tenga un codigo de barras y aduanas unico",
        request_body=ItemShopCartCreateSerializer,
    )
    def post(self, request):
        serializer = ItemShopCartCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
