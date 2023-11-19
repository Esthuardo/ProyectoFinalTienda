from rest_framework import status
from rest_framework.viewsets import generics
from rest_framework.response import Response
from authenticationClient.permissions import ClientIsAuthenticated, ClientAuthentication
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from .models import Shopping_cart
from .serializers import (
    ShoppingCartSerializer,
    ShoppingCartUpdateSerializer,
    ShoppingCartCreateSerializer,
)

# Create your views here.


class ShoppingCartView(generics.GenericAPIView):
    serializer_class = ShoppingCartSerializer
    http_method_names = ["get", "post"]
    authentication_classes = [ClientAuthentication]
    permission_classes = [ClientIsAuthenticated]

    def get_queryset(self):
        return Shopping_cart.objects.none()

    @swagger_auto_schema(
        operation_summary="Endpoint para listar todos los productos activos",
        operation_description="Retoma una lista de productos",
    )
    def get(self, request):
        record = Shopping_cart.objects.all().order_by("client")
        serializer = self.get_serializer(record, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para crear un método de pago",
        operation_description="Crea una método de pago que tenga un nombre unico",
    )
    def post(self, request):
        serializer = ShoppingCartCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShoppingCartByClientIDView(generics.GenericAPIView):
    serializer_class = ShoppingCartSerializer
    http_method_names = ["get"]
    authentication_classes = [ClientAuthentication]
    permission_classes = [ClientIsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Endpoint para listar el carrito del cliente",
        operation_description="Retoma la lista el carrito del cliente",
    )
    def get(self, _, id):
        record = Shopping_cart.objects.filter(client=id).order_by("client")
        record = get_object_or_404(Shopping_cart, client=id)
        serializer = self.serializer_class(record)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShoppingCartByIdView(generics.GenericAPIView):
    serializer_class = ShoppingCartUpdateSerializer
    http_method_names = ["get", "patch"]
    authentication_classes = [ClientAuthentication]
    permission_classes = [ClientIsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Endpoint para obtener un producto en especifico",
        operation_description="En este servicio encontramos un producto por su id",
    )
    def get(self, _, id):
        record = get_object_or_404(Shopping_cart, pk=id)
        serializer = ShoppingCartSerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para actualizar un producto",
        operation_description="En este servicio cambiamos los datos de un producto",
    )
    def patch(self, request, id):
        record = get_object_or_404(Shopping_cart, pk=id)
        serializer = ShoppingCartUpdateSerializer(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
