from django.http import HttpResponse
from django.conf import settings

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import MoviesSerializer
from .models import Movies
from .filters import MoviesFilter


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


class MovieListView(ListAPIView):
    serializer_class = MoviesSerializer
    filterset_class = MoviesFilter
    # Enable sorting the movies by time_stamp and seconds
    ordering_fields = ["time_stamp", "seconds"]
    ordering = ["time_stamp"]

    def get_queryset(self):
        return Movies.objects.all()

    def paginate_queryset(self, queryset):

        # Get the DEBUG setting from the settings.py file
        DEBUG = getattr(settings, "DEBUG", True)

        # Set the current_scheme_host to the correct value based on the DEBUG setting
        if DEBUG:
            # Local development setting
            self.request._request._current_scheme_host = "http://127.0.0.1"
        else:
            # Production setting
            self.request._request._current_scheme_host = "https://winearth.sdsc.edu"

        return super().paginate_queryset(queryset)


@api_view(["GET"])
def movie_details(request, movie_name):
    try:
        movie = Movies.objects.get(movie=movie_name)
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)


@api_view(["GET"])
def version(request):
    return Response({"version": "0.2.0"})
