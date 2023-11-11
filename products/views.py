from .models import Product
from .serializers import ProductsSerializer, ProductCreateSerializer
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
        manual_parameters=schema.all(),
    )
    def get(self, request):
        page = request.query_params.get("page", 1)
        per_page = request.query_params.get("per_page", 8)
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
        request_body=ProductCreateSerializer,
    )
    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
