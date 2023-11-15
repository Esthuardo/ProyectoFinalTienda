from .models import PaymentMethod
from .serializers import (
    PaymentMethodSerializer,
    PaymentMethodCreateSerializer,
    PaymentMethodUpdateSerializer,
)
from rest_framework import status
from rest_framework.viewsets import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from services.enableTables import Element
from services.validations import ReactivateSerializer

element = Element()

# Operaciones para ver y crear métodos de pago


class PaymentMethodView(generics.GenericAPIView):
    serializer_class = PaymentMethodSerializer
    http_method_names = ["get", "post"]

    @swagger_auto_schema(
        operation_summary="Endpoint para listar todos los métodos de pago activos",
        operation_description="Retoma una lista de los métodos de pago",
    )
    def get(self, request):
        record = PaymentMethod.objects.all().exclude(status=False).order_by("name")
        serializer = self.get_serializer(record, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para crear un método de pago",
        operation_description="Crea una método de pago que tenga un nombre unico",
    )
    def post(self, request):
        serializer = PaymentMethodCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Operaciones con un método de pago con su ID


class PaymentMethodByIdView(generics.GenericAPIView):
    serializer_class = PaymentMethodUpdateSerializer
    http_method_names = ["get", "patch", "delete"]

    @swagger_auto_schema(
        operation_summary="Endpoint para obtener un método de pago en especifico",
        operation_description="En este servicio encontramos un método de pago por su id",
    )
    def get(self, _, id):
        record = get_object_or_404(PaymentMethod, pk=id, status=True)
        serializer = self.serializer_class(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para actualizar el nombre de un método de pago",
        operation_description="En este servicio cambiamos el nombre de un método de pago por otro unico",
    )
    def patch(self, request, id):
        record = get_object_or_404(PaymentMethod, pk=id, status=True)
        serializer = PaymentMethodUpdateSerializer(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para inhabilitar un método de pago por el ID",
        operation_description="En este servicio podemos inhabilitar un método de pago por el ID",
    )
    def delete(self, _, id):
        element.disableElement(PaymentMethod, id)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


# Reactivar un método de pago en caso sea necesario


class PaymentMethodReactivateView(generics.GenericAPIView):
    serializer_class = ReactivateSerializer
    http_method_names = ["patch"]

    @swagger_auto_schema(
        operation_summary="Endpoint para reactivar un método de pago",
        operation_description="En este servicio reactivamos un método de pago por su id",
    )
    def patch(self, _, id):
        message = element.enableElement("Método de pago", PaymentMethod, id)
        return Response(
            message,
            status=status.HTTP_200_OK,
        )
