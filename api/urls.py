from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/", views.movie_list, name="movie_list"),
    path("movies/<str:movie_name>/", views.movie_details, name="movie_details"),
    path("version/", views.version, name="version"),
]
