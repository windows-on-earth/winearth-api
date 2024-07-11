from rest_framework import serializers
from .models import Movies


class MoviesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movies
        fields = [
            "movie",
            "url",
            "url_rt",
            "iis_mission",
            "time_stamp",
            "seconds",
            "images",
            "start_latitude",
            "start_longitude",
            "end_latitude",
            "end_longitude",
            "model",
            "lens",
            "iso",
            "shutter_speed",
            "f_number",
        ]
