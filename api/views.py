import re
import time
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .serializers import MoviesSerializer
from .models import Movies
from .mypaginations import MoviesPagination


def validate_date(date_str):
    date_regex = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/([0-9]{4})$"
    if not re.match(date_regex, date_str):
        raise ValidationError(
            f"Date {date_str} is not in the correct format MM/DD/YYYY."
        )


def validate_length(length_str):
    length_regex = r"^\d+$"
    if not re.match(length_regex, length_str):
        raise ValidationError(f"length {length_str} is not in the correct format.")


def filter_movies_by_date(movie, start_date, end_date):

    if start_date:
        # Validate the date format
        validate_date(start_date)

        # Convert the date string to datetime object
        start_date = datetime.strptime(start_date, "%m/%d/%Y")

        # Convert the datetime object to unix timestamp
        start_timestamp = int(time.mktime(start_date.timetuple()))

        # Filter the movies by the timestamp
        movie = movie.filter(time_stamp__gte=start_timestamp)

    if end_date:
        # Validate the date format
        validate_date(end_date)

        # Convert the date string to datetime object
        end_date = datetime.strptime(end_date, "%m/%d/%Y")

        # Convert the datetime object to unix timestamp
        end_timestamp = int(time.mktime(end_date.timetuple()))

        # Filter the movies by the timestamp
        movie = movie.filter(time_stamp__lte=end_timestamp)

    return movie


def filter_movies_by_length(movie, min, max):
    if min:
        # Validate the length format
        validate_length(min)
        movie = movie.filter(seconds__gte=min)
    if max:
        # Validate the length format
        validate_length(max)
        movie = movie.filter(seconds__lte=max)

    return movie


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


@api_view(["GET"])
def movie_list(request):

    if request.method == "GET":
        movie = Movies.objects.all()


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
    return Response({"version": "0.1.6"})