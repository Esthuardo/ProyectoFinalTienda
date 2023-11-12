from django.urls import path
from .views import (
    ProductView,
    ProductByIdView,
    ProductReactivateView,
    ProductSearchByNameView,
)

urlpatterns = [
    path("", ProductView.as_view(), name="list_products"),
    path("<int:id>/", ProductByIdView.as_view(), name="product_by_id"),
    path("<int:id>/reactivate", ProductReactivateView.as_view(), name="reactivate"),
    path("name/<str:name>/", ProductSearchByNameView.as_view(), name="product_by_name"),
]
