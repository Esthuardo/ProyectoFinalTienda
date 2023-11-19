from drf_yasg import openapi
from django.urls import path
from drf_yasg.views import get_schema_view

views = get_schema_view(
    openapi.Info(
        title="CRUD_Tienda",
        default_version="0.8v",
        description="Documentación de los endpoints del CRUD",
    ),
    public=True,
)

urlpatterns = [path("swagger-ui/", views.with_ui("swagger"), name="swagger-ui")]
