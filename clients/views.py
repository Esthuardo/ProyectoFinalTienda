from .serializers import (
    ClientSerializer,
    ClientCreateSerializer,
    ClientUpdateSerializer,
)
from .models import Client
from .schemas import ClientSchema
from rest_framework import status
from rest_framework.viewsets import generics
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from services.paginateTables import PaginateTable
from services.validateUnique import ReactivateSerializer
from services.enableTables import Element

schema = ClientSchema()
paginate = PaginateTable()
element = Element()


class ClientView(generics.GenericAPIView):
    serializer_class = ClientSerializer
    http_method_names = ["get", "post"]

    @swagger_auto_schema(
        operation_summary="Endpoint para listar a los clientes ",
        operation_description="Retorna la lista de clientes",
        manual_parameters=schema.all,
    )
    def get(self, request):
        record = Client.objects.all().order_by("id")
        data = paginate.pagination(request, record, self.serializer_class)
        return Response(
            data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_summary="Endpoint para crear un cliente",
        operation_description="Crea un cliente",
        request_body=ClientCreateSerializer,
    )
    def post(self, request):
        serializer = ClientCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Manejo de clientes por su id
class ClientGetByIdView(generics.GenericAPIView):
    serializer_class = ClientSerializer
    http_method_names = ["get", "patch", "delete"]

    @swagger_auto_schema(
        operation_summary="Endpoint para obtener un usuario especifico",
        operation_description="En este servicio encontramos a un usuario y vemos sus datos",
    )
    def get(self, _, id):
        record = get_object_or_404(Client, pk=id, status=True)
        serializer = self.serializer_class(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoitn para actualizar los datos de un usuario",
        operation_description="En este servicio encontramos a un usuario y vemos sus datos",
        request_body=ClientUpdateSerializer,
    )
    def patch(self, request, id):
        record = get_object_or_404(Client, pk=id, status=True)
        serializer = ClientUpdateSerializer(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para inhabilitar un usuario por el ID",
        operation_description="En este servicio podemos inhabilitar un usuario por el ID",
    )
    def delete(self, _, id):
        element.disableElement(Client, id)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


# Reactivar el cliente en caso sea necesario


class ClientReactivateView(generics.GenericAPIView):
    serializer_class = ReactivateSerializer
    http_method_names = ["patch"]

    @swagger_auto_schema(
        operation_summary="Endpoint para reactivar un usuario",
        operation_description="En este servicio reactivamos un usuario por su id",
    )
    def patch(self, _, id):
        record = get_object_or_404(Client, pk=id, status=False)
        record.is_active = True
        record.save()
        return Response(
            {"message": f"Usuario {record.name} habilitado"},
            status=status.HTTP_200_OK,
        )
