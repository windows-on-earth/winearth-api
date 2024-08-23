from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class MoviesPagination(LimitOffsetPagination):
  default_limit = 100
  max_limit = 20
  DEV_MODE = False # Change to true when running standalone docker container for winearth-api
  host = 'http://127.0.0.1' if DEV_MODE else 'https://winearth.sdsc.edu'

  def get_paginated_response(self, data):
    nl = self.get_next_link()
    print(f'next link: {nl}')
    pl = self.get_previous_link()
    print(f'prev link: {pl}')
    return Response({
      'next': 'http://127.0.0.1' + nl[nl.find("/api") : ] if nl is not None else None,
      'previous': 'http://127.0.0.1' + pl[pl.find("/api") : ] if pl is not None else None,
      'count': self.count,
      'results': data
    })