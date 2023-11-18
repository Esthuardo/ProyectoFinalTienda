from django.urls import path
from .views import (
    RegisterClientView,
    LoginClientView,
    RefresClientTokenView,
    # ClientLogOut,
)

urlpatterns = [
    path("signup/", RegisterClientView.as_view(), name="signup"),
    path("signin/", LoginClientView.as_view(), name="signin"),
    path("token/refresh/", RefresClientTokenView.as_view(), name="refresh_token"),
    # path("logout/", ClientLogOut.as_view(), name="log_out")
    # path("password/reset", ResetPasswordView.as_view(), name="reset_password"),
]
