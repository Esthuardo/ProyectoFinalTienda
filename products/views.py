from .models import Product
from .serializers import (
    ProductsSerializer,
    ProductsCreateSerializer,
    ProductsUpdateSerializer,
    ProductsSearchByNameSerializer,
)
from .schemas import ProductsSchema
from rest_framework import status, permissions
from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from services.paginateTables import PaginateTable
from services.enableTables import Element
from services.validations import ReactivateSerializer

schema = ProductsSchema()
paginate = PaginateTable()
element = Element()

# Obtener los productosy agregar nuevos


class ProductView(generics.GenericAPIView):
    serializer_class = ProductsSerializer
    http_method_names = ["get", "post"]

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super(ProductView, self).get_permissions()

    @swagger_auto_schema(
        operation_summary="Endpoint para listar todos los productos activos",
        operation_description="Retoma una lista de productos",
        manual_parameters=schema.all,
    )
    def get(self, request):
        record = Product.objects.filter(status=True).order_by("name")
        data = paginate.pagination(request, record, self.serializer_class)
        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para crear un producto",
        operation_description="Crea un nuevo producto que tenga un codigo de barras y aduanas unico",
        request_body=ProductsCreateSerializer,
    )
    def post(self, request):
        serializer = ProductsCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Operaciones con los productos usando su ID


class ProductByIdView(generics.GenericAPIView):
    serializer_class = ProductsUpdateSerializer
    http_method_names = ["get", "patch", "delete"]

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(ProductByIdView, self).get_permissions()

    @swagger_auto_schema(
        operation_summary="Endpoint para obtener un producto en especifico",
        operation_description="En este servicio encontramos un producto por su id",
    )
    def get(self, _, id):
        record = get_object_or_404(Product, pk=id, status=True)
        serializer = self.serializer_class(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para actualizar un producto",
        operation_description="En este servicio cambiamos los datos de un producto",
    )
    def patch(self, request, id):
        record = get_object_or_404(Product, pk=id, status=True)
        serializer = ProductsUpdateSerializer(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Endpoint para inhabilitar un producto por el ID",
        operation_description="En este servicio podemos inhabilitar un producto por el ID",
    )
    def delete(self, _, id):
        element.disableElement(Product, id)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class ProductByCategory(generics.GenericAPIView):
    serializer_class = ProductsSerializer
    http_method_names = ["get"]

    @swagger_auto_schema(
        operation_summary="Endpoint para los productos por categoria",
        operation_description="En este servicio encontramos los productos por categoria",
        manual_parameters=schema.all,
    )
    def get(self, request, category):
        record = Product.objects.filter(status=True, category=category).order_by("name")
        data = paginate.pagination(request, record, self.serializer_class)
        return Response(data, status=status.HTTP_200_OK)


# Reactivar un producto


class ProductReactivateView(generics.GenericAPIView):
    serializer_class = ReactivateSerializer
    http_method_names = ["patch"]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Endpoint para habilitar nuevamente un producto",
        operation_description=" En este servicios habilitamos un producto por su id",
    )
    def patch(self, _, id):
        message = element.enableElement("Producto", Product, id)
        return Response(message, status=status.HTTP_200_OK)


# Buscar un producto por su nombre


class ProductSearchByNameView(generics.GenericAPIView):
    serializer_class = ProductsSearchByNameSerializer
    http_method_names = ["get"]

    @swagger_auto_schema(
        operation_summary="Endpoint para encontrar un producto por su nombre",
        operation_description=" En este servicios encontramos un producto por su atributo name",
    )
    def get(self, request, name):
        record = Product.objects.filter(name__icontains=name, status=True)
        if not record.exists():
            raise NotFound(
                "No se encontró ningún producto con el nombre proporcionado."
            )
        data = paginate.pagination(request, record, self.serializer_class)
        return Response(
            {
                "results": data["results"],
            },
            status=status.HTTP_200_OK,
        )
