from rest_framework.pagination import LimitOffsetPagination

class MoviesPagination(LimitOffsetPagination):
  default_limit = 100
  max_limit = 20

  def get_paginated_response(self, data):
    return super().get_paginated_response(data)