from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MoviesSerializer
from .models import Movies
from .mypaginations import MoviesPagination


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


@api_view(["GET"])
def movie_list(request):

    if request.method == "GET":
        movie = Movies.objects.all()

        # Instantiate movies pagination class
        paginator = MoviesPagination()

        # Paginate queryset
        paginated_movies = paginator.paginate_queryset(movie, request)

        # Serialize paginated data
        serializer = MoviesSerializer(paginated_movies, many=True)

        # Return paginated response
        return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
def movie_details(request, movie_name):
    try:
        movie = Movies.objects.get(movie=movie_name)
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)
