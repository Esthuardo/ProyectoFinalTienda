from django.core.exceptions import ValidationError
from clients.models import Client
from rest_framework.permissions import BasePermission


def authenticate_client(email=None, password=None):
    try:
        client = Client.objects.get(email=email)
        if client.check_password(password):
            return client
    except Client.DoesNotExist:
        raise ValidationError("Client with given email and password does not exist")
    return None


class ClientIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        email = request.data.get("email")
        password = request.data.get("password")
        client = authenticate_client(email=email, password=password)
        return client is not None
