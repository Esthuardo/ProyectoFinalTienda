from django.urls import path
from .views import CategoryView, CategoryByIdView, CategoryReactivateView

urlpatterns = [
    path("", CategoryView.as_view(), name="list_categories"),
    path("<int:id>/", CategoryByIdView.as_view(), name="category_by_id"),
    path("<int:id>/reactivate", CategoryReactivateView.as_view(), name="reactivate"),
]
