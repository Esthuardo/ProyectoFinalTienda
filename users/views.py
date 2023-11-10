# from django.shortcuts import render
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from .schemas import UserSchema
from rest_framework import status
from rest_framework.viewsets import generics
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from rest_framework.response import Response

# Create your views here.
schema = UserSchema()


class UserView(generics.GenericAPIView):
    serializer_class = UserSerializer
    http_method_names = ["get", "post"]

    @swagger_auto_schema(
        operation_summary="Endpoint para listar a los Usuarios trabajadores",
        operation_description="Retorna la lista de trabajadores",
        manual_parameters=schema.all(),
    )
    def get(self, request):
        page = request.query_params.get("page")
        per_page = request.query_params.get("per_page")
        record = User.objects.all().order_by("id")

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

    @swagger_auto_schema(
        operation_summary="Endpoint para listar a los Usuarios trabajadores",
        operation_description="Retorna la lista de trabajadores",
        request_body=UserCreateSerializer,
    )
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserGetByIdView(generics.GenericAPIView):
    serializer_class = UserSerializer
    http_method_names = ["get", "patch", "delete"]

    @swagger_auto_schema(
        operation_summary="Endpoint para obtener un usuario especifico",
        operation_description="En este servicio encontramos a un usuario y vemos sus datos",
    )
    def get(self, _, id):
        record = get_object_or_404(
            User, pk=id, is_active=True, is_staff=False, status=True
        )
        serializer = self.serializer_class(record)
        return Response(serializer.data, status=status.HTTP_200_OK)
