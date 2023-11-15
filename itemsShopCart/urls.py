from django.urls import path
from .views import ItemShopView

urlpatterns = [
    path("", ItemShopView.as_view(), name="list_products_cart"),
    # path("<int:id>/", ProductByIdView.as_view(), name="product_by_id"),
    # path("<int:id>/reactivate", ProductReactivateView.as_view(), name="reactivate"),
    # path("name/<str:name>/", ProductSearchByNameView.as_view(), name="product_by_name"),
]
