from drf_yasg import openapi


class ProductsSchema:
    def all(self):
        page = openapi.Parameter(
            "page", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=1
        )
        per_page = openapi.Parameter(
            "per_page", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=8
        )
        return [page, per_page]
