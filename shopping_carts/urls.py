from django.urls import path
from .views import ShoppingCartView

urlpatterns = [
    path("", ShoppingCartView.as_view(), name="list_payment_method"),
]
