from django.core.exceptions import ValidationError
from clients.models import Client
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from django.contrib.auth import get_user_model


def authenticate_client(email=None, password=None):
    try:
        client = Client.objects.get(email=email)
        if client.status and client.check_password(password):
            return client
    except Client.DoesNotExist:
        raise ValidationError("Client with given email and password does not exist")
    return None


class ClientAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token

    def get_user(self, validated_token):
        try:
            client_id = validated_token["user_id"]
        except KeyError:
            raise InvalidToken("Token contains no valid user identification")
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            raise AuthenticationFailed("Client not found")
        if not client.status:
            raise AuthenticationFailed("Client is inactive")

        return client


class ClientIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user is not None and isinstance(request.user, Client)
