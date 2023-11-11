from django.urls import path
from .views import ProductView

urlpatterns = [
    path("", ProductView.as_view(), name="list_products"),
    # path("<int:id>/", CategoryByIdView.as_view(), name="category_by_id"),
    # path("<int:id>/reactivate", CategoryReactivateView.as_view(), name="reactivate"),
]
