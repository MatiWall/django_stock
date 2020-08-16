from rest_framework import pagination
from rest_framework.response import Response

from collections import OrderedDict
class customPagination(pagination.PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):
        return Response({
            'lastPage': self.page.paginator.num_pages,
            'countItemsOnPage': self.page_size,
            'current' : self.page.number,
             'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
             },
             'results': data
        })

