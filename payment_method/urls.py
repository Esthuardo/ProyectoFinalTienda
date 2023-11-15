from django.urls import path
from .views import PaymentMethodView, PaymentMethodByIdView, PaymentMethodReactivateView

urlpatterns = [
    path("", PaymentMethodView.as_view(), name="list_payment_method"),
    path("<int:id>/", PaymentMethodByIdView.as_view(), name="payment_method_by_id"),
    path(
        "<int:id>/reactivate", PaymentMethodReactivateView.as_view(), name="reactivate"
    ),
]
