from .models import ItemShopCart
from .serializers import (
    ItemShopCartSerializer,
    ItemShopCartCreateSerializer,
    ItemShopUpdateSerializer,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import generics
from authenticationClient.permissions import ClientIsAuthenticated, ClientAuthentication
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


class ItemShopView(generics.GenericAPIView):
    serializer_class = ItemShopCartSerializer
    queryset = ItemShopCart.objects.all()
    http_method_names = ["get", "post"]
    authentication_classes = []
    permission_classes = []

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


class ItemShopSearchView(generics.GenericAPIView):
    serializer_class = ItemShopCartSerializer
    http_method_names = ["get", "patch"]
    authentication_classes = [ClientAuthentication]
    permission_classes = [ClientIsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Endpoint para verificar si un producto existe en la lista de IDs",
        operation_description="En este servicio verificamos si un producto con un ID específico existe en la lista de IDs proporcionada",
    )
    def get(self, request):
        ids = request.GET.getlist("ids")
        ids = [int(id) for id in ids]
        product_id = request.GET.get("product_id")
        try:
            product = ItemShopCart.objects.get(id__in=ids, product=product_id)
            return Response(
                {
                    "message": f"El producto con ID {product.id} tiene product_id en su campo product",
                    "itemShop_id": product.id,
                },
                status=status.HTTP_200_OK,
            )
        except ItemShopCart.DoesNotExist:
            return Response(
                {
                    "message": "No existe un producto con esos ID que tenga product_id en su campo product"
                },
                status=status.HTTP_404_NOT_FOUND,
            )


class ItemShopByIdView(generics.GenericAPIView):
    serializer_class = ItemShopUpdateSerializer
    http_method_names = ["get", "patch"]
    authentication_classes = [ClientAuthentication]
    permission_classes = [ClientIsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Endpoint para actualizar un producto en carrito",
        operation_description="En este servicio cambiamos los datos de un producto en carrito",
    )
    def get(self, _, id):
        record = get_object_or_404(ItemShopCart, pk=id)
        serializer = ItemShopCartSerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para actualizar un producto en carrito",
        operation_description="En este servicio cambiamos los datos de un producto en carrito",
    )
    def patch(self, request, id):
        record = get_object_or_404(ItemShopCart, pk=id)
        serializer = self.serializer_class(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
