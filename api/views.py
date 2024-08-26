import re
import time
import urllib.parse  # Useful for decoding URLs
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


def validate_integers(str: str, validated_value: str):
    integer_regex = r"^\d+$"
    if not re.match(integer_regex, str):
        raise ValidationError(f"{validated_value} {str} is not in the correct format. Please use only non-negative integers.")


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


# Filters movies by length in seconds
def filter_movies_by_length(movie, min, max):
    if min:
        # Validate the length format
        validate_integers(min, 'length')
        movie = movie.filter(seconds__gte=min)
    if max:
        # Validate the length format
        validate_integers(max, 'length')
        movie = movie.filter(seconds__lte=max)

    return movie


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


# Returns a list of movies that can vary with different parameters
# Can filter movies by date using the url params "start_date" and "end_date" in
#   MM/DD/YYYY format
# Example: http://127.0.0.1/api/movies/?start_date=10/31/2011&end_date=12/31/2011
# Can filter movies by length using the url params "min_length" and "max_length"
#   in seconds
# Example: http://127.0.0.1/api/movies/?min_length=500&max_length=900
# Can paginate query set to only return up to url param "limit" as int and offset the
#   resulting list with url param "offset" as int
# Example: http://127.0.0.1/api/movies/?limit=5&offset=5
# An example of an advanced query:
#   http://127.0.0.1/api/movies/?start_date=10/31/2011&end_date=12/31/2011&min_length=500&max_length=900&limit=2&offset=2
@api_view(["GET"])
def movie_list(request):

    if request.method == "GET":
        movie = Movies.objects.all()

        # Filter the movies by date
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        if start_date or end_date:
            movie = filter_movies_by_date(movie, urllib.parse.unquote(start_date), urllib.parse.unquote(end_date))

        # Filter the movies by length
        min_length = request.query_params.get("min_length")
        max_length = request.query_params.get("max_length")

        if min_length or max_length:
            movie = filter_movies_by_length(movie, urllib.parse.unquote(min_length), urllib.parse.unquote(max_length))

        # Instantiate movies pagination class
        paginator = MoviesPagination()

        # Paginate queryset
        limit = request.query_params.get("limit")
        if limit:
            limit = urllib.parse.unquote(limit)
            validate_integers(limit, 'limit')
        offset = request.query_params.get("offset")
        if offset:
            offset = urllib.parse.unquote(offset)
            validate_integers(offset, 'offset')

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


@api_view(["GET"])
def version(request):
    return Response({"version": "0.1.7"})
