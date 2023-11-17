from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("signin/", LoginView.as_view(), name="signin"),
    # path("token/refresh/", RefresTokenView.as_view(), name="refresh_token"),
    # path("password/reset", ResetPasswordView.as_view(), name="reset_password"),
]
