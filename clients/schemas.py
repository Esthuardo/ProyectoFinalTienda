from drf_yasg import openapi


class ClientSchema:
    @property
    def all(self):
        page = openapi.Parameter(
            "page", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=1
        )
        per_page = openapi.Parameter(
            "per_page", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=10
        )
        return [page, per_page]
