from django.urls import path
from .views import RegisterClientView, LoginClientView

urlpatterns = [
    path("signup/", RegisterClientView.as_view(), name="signup"),
    path("signin/", LoginClientView.as_view(), name="signin"),
    # path("token/refresh/", RefresTokenView.as_view(), name="refresh_token"),
    # path("password/reset", ResetPasswordView.as_view(), name="reset_password"),
]
