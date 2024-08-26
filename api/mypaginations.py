from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class MoviesPagination(LimitOffsetPagination):
  default_limit = 100
  max_limit = 20

  def get_paginated_response(self, data):
    DEV_MODE = False # Change to true when running standalone docker container for winearth-api
    HOST = 'http://127.0.0.1' if DEV_MODE else 'https://winearth.sdsc.edu'

    nl = self.get_next_link()
    pl = self.get_previous_link()
    return Response({
      'next': HOST + nl[nl.find("/api") : ] if nl is not None else None,
      'previous': HOST + pl[pl.find("/api") : ] if pl is not None else None,
      'count': self.count,
      'results': data
    })