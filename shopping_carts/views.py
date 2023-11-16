from rest_framework import status
from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from .models import Shopping_cart
from .serializers import ShoppingCartSerializer, ShoppingCartCreateSerializer

# Create your views here.


class ShoppingCartView(generics.GenericAPIView):
    serializer_class = ShoppingCartSerializer
    http_method_names = ["get", "post"]

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
