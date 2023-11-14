from django.core.paginator import Paginator


class PaginateTable:
    def pagination(self, request, record, serializer_class):
        page = request.query_params.get("page", 1)
        per_page = request.query_params.get("per_page", 8)
        pagination = Paginator(record, per_page=per_page)
        nro_page = pagination.get_page(page)
        serializer = serializer_class(nro_page.object_list, many=True)
        return {
            "results": serializer.data,
            "pagination": {
                "totalRecords": pagination.count,
                "totalPages": pagination.num_pages,
                "perPage": pagination.per_page,
                "currentPage": nro_page.number,
            },
        }
