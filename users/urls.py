from django.urls import path
from .views import UserView, UserGetByIdView, UserReactivateView, UserDeleteView

urlpatterns = [
    path("", UserView.as_view(), name="list_users"),
    path("<int:id>/", UserGetByIdView.as_view(), name="user_by_id"),
    path("<int:id>/reactivate/", UserReactivateView.as_view(), name="control_users"),
    path("<int:id>/delete/", UserDeleteView.as_view(), name="control_users"),
]
