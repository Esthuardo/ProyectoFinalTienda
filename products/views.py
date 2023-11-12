from .models import Product
from .serializers import (
    ProductsSerializer,
    ProductsCreateSerializer,
    ProductsUpdateSerializer,
    ProductsReactivateSerializer,
    ProductsSearchByNameSerializer,
)
from .schemas import ProductsSchema
from rest_framework import status
from rest_framework.viewsets import generics
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


schema = ProductsSchema()


class ProductView(generics.GenericAPIView):
    serializer_class = ProductsSerializer
    http_method_names = ["get", "post"]

    @swagger_auto_schema(
        operation_summary="Endpoint para listar todos los productos activos",
        operation_description="Retoma una lista de productos",
        manual_parameters=schema.all,
    )
    def get(self, request):
        page = request.query_params.get("page")
        per_page = request.query_params.get("per_page")
        record = Product.objects.all().exclude(status=False).order_by("name")

        pagination = Paginator(record, per_page=per_page)
        nro_page = pagination.get_page(page)
        serializer = self.serializer_class(nro_page.object_list, many=True)

        return Response(
            {
                "results": serializer.data,
                "pagination": {
                    "totalRecords": pagination.count,
                    "totalPages": pagination.num_pages,
                    "perPage": pagination.per_page,
                    "currentPage": nro_page.number,
                },
            },
            status=status.HTTP_200_OK,
        )

    def get_queryset(self):
        return Product.objects.all().exclude(status=False).order_by("name")

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


class ProductByIdView(generics.GenericAPIView):
    serializer_class = ProductsUpdateSerializer
    http_method_names = ["get", "patch", "delete"]

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
        record = get_object_or_404(Product, pk=id, status=True)
        record.status = False
        record.save()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class ProductReactivateView(generics.GenericAPIView):
    serializer_class = ProductsReactivateSerializer
    http_method_names = ["patch"]

    @swagger_auto_schema(
        operation_summary="Endpoint para habilitar nuevamente un producto",
        operation_description=" En este servicios habilitamos un producto por su id",
    )
    def patch(self, _, id):
        record = get_object_or_404(Product, pk=id, status=False)
        record.status = True
        record.save()
        return Response(
            {"message": f"Producto {record.name} habilitado"},
            status=status.HTTP_200_OK,
        )


class ProductSearchByNameView(generics.GenericAPIView):
    serializer_class = ProductsSearchByNameSerializer
    http_method_names = ["get"]

    @swagger_auto_schema(
        operation_summary="Endpoint para encontrar un producto por su nombre",
        operation_description=" En este servicios encontramos un producto por su atributo name",
        manual_parameters=schema.all,
    )
    def get(self, request, name):
        page = request.query_params.get("page")
        per_page = request.query_params.get("per_page")
        record = Product.objects.filter(name__icontains=name, status=True)

        pagination = Paginator(record, per_page=per_page)
        nro_page = pagination.get_page(page)
        serializer = self.serializer_class(nro_page.object_list, many=True)
        return Response(
            {
                "results": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
