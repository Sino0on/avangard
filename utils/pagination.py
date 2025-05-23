from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MyCustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': self.page.number,
            # 'pages': self.page_size,
            'limit': self.get_page_size(self.request),
            'results': data
        })
