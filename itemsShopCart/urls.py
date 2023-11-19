from django.urls import path
from .views import ItemShopView, ItemShopSearchView, ItemShopByIdView

urlpatterns = [
    path("", ItemShopView.as_view(), name="list_products_cart"),
    path("search/", ItemShopSearchView.as_view(), name="productItem_search"),
    path("<int:id>/", ItemShopByIdView.as_view(), name="patch_by_id"),
    # path("name/<str:name>/", ProductSearchByNameView.as_view(), name="product_by_name"),
]
