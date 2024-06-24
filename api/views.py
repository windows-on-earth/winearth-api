from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MoviesSerializer
from .models import Movies


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


@api_view(["GET"])
def movie_list(request):

    if request.method == "GET":
        movie = Movies.objects.all()
        serializer = MoviesSerializer(movie, many=True)
        return Response(serializer.data)
