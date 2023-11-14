from django.urls import path
from .views import ClientView, ClientGetByIdView, ClientReactivateView

urlpatterns = [
    path("", ClientView.as_view(), name="list_users"),
    path("<int:id>/", ClientGetByIdView.as_view(), name="user_by_id"),
    path("<int:id>/reactivate/", ClientReactivateView.as_view(), name="control_users"),
]
