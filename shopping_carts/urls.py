from django.urls import path
from .views import ShoppingCartView, ShoppingCartByIdView, ShoppingCartByClientIDView

urlpatterns = [
    path("", ShoppingCartView.as_view(), name="list_payment_method"),
    path("<int:id>/", ShoppingCartByIdView.as_view(), name="SC_by_id"),
    path("client/<int:id>/", ShoppingCartByClientIDView.as_view(), name="SC_by_client"),
]
