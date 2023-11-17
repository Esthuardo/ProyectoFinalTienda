from rest_framework.request import Request
from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegisterSerializer, LoginSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


# Registro - POST - 201
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    http_method_names = ["post"]

    @swagger_auto_schema(
        operation_summary="Endpoint para registrar los usuarios",
        operation_description="En este servicio se podra crear un usuario nuevo",
        security=[],
    )
    def post(self, request):
        # Instanciar el serializador con los datos del bodyrequest
        serializer = self.serializer_class(data=request.data)
        # Iniciamos la validación del serializador
        serializer.is_valid(raise_exception=True)
        # Ejecutamos la orden 66 digo la acción
        # Sea creacion, actualización o eliminacion si o si se llaman por el metodo save
        serializer.save()
        # retornamos la respuesta
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Login - POST - 200
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    http_method_names = ["post"]

    @swagger_auto_schema(
        operation_summary="Endpoint para logear al usuario",
        operation_description="En este servicio el usuario podra logearse con su username and password",
        security=[],
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# # Refresh Token - POST - 200
# class RefresTokenView(TokenViewBase):
#     serializer_class = TokenRefreshSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [JWTAuthentication]

#     @swagger_auto_schema(
#         operation_summary="Endpoint para generar un access token",
#         operation_description="En este servicio podemnos generar un nuevo access_token desde el refren token",
#     )
#     def post(self, request):
#         return super().post(request)

#     # Reinicio contraseña - POST - 201
#     # class ResetPasswordView(generics.GenericAPIView):
#     serializer_class = ResetPasswordSerializer

#     @swagger_auto_schema(
#         operation_summary="Endpoint para resetear la contraseña",
#         operation_description="En este servicio podemnos reiniciar la contraseña y que a su vez no llegue un correo con la nueva",
#         security=[],
#     )
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
