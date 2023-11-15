from .models import Category
from .serializers import (
    CategorieSerializer,
    CategorieCreateSerializer,
    CategorieUpdateSerializer,
)
from .schemas import CategorySchema
from rest_framework import status
from rest_framework.viewsets import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from services.paginateTables import PaginateTable
from services.enableTables import Element
from services.validations import ReactivateSerializer

schema = CategorySchema()
paginate = PaginateTable()
element = Element()

# Operaciones para ver y crear categorias


class CategoryView(generics.GenericAPIView):
    serializer_class = CategorieSerializer
    http_method_names = ["get", "post"]

    @swagger_auto_schema(
        operation_summary="Endpoint para listar todas las categorias activas",
        operation_description="Retoma una lista de categorias de los productos",
        manual_parameters=schema.all,
    )
    def get(self, request):
        record = Category.objects.all().exclude(status=False).order_by("name")
        data = paginate.pagination(request, record, self.serializer_class)
        return Response(
            data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_summary="Endpoint para crear una categoria",
        operation_description="Crea una nueva categoria que tenga un nombre unico",
    )
    def post(self, request):
        serializer = CategorieCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Operaciones con la categoria con su ID


class CategoryByIdView(generics.GenericAPIView):
    serializer_class = CategorieUpdateSerializer
    http_method_names = ["get", "patch", "delete"]

    @swagger_auto_schema(
        operation_summary="Endpoint para obtener una categoria en especifico",
        operation_description="En este servicio encontramos una categoria por su id",
    )
    def get(self, _, id):
        record = get_object_or_404(Category, pk=id, status=True)
        serializer = self.serializer_class(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para actualizar el nombre de una categoria",
        operation_description="En este servicio cambiamos el nombre de una categoria por otro unico",
    )
    def patch(self, request, id):
        record = get_object_or_404(Category, pk=id, status=True)
        serializer = CategorieUpdateSerializer(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para inhabilitar una categoria por el ID",
        operation_description="En este servicio podemos inhabilitar una categoria por el ID",
    )
    def delete(self, _, id):
        element.disableElement(Category, id)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


# Reactivar la categoria en caso sea necesario


class CategoryReactivateView(generics.GenericAPIView):
    serializer_class = ReactivateSerializer
    http_method_names = ["patch"]

    @swagger_auto_schema(
        operation_summary="Endpoint para reactivar una categoria",
        operation_description="En este servicio reactivamos una categoria por su id",
    )
    def patch(self, _, id):
        message = element.enableElement("Categoria", Category, id)
        return Response(
            message,
            status=status.HTTP_200_OK,
        )
