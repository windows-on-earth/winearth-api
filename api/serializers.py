from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = [
            "nasa_filename",
            "woe_filename",
            "date_time_imported",
            "date_time_captured",
            "nasa_expidition",
            "iss_latitude",
            "iss_longitude",
            "iss_altitude",
            "iss_velocity",
            "iss_geom",
            "iss_3d_geom",
            "target_latitude",
            "target_longitude",
            "target_altitude",
            "target_geom",
            "exif_data",
            "exif_processed",
            "camera_fov",
            "camera_orientation",
            "camera",
            "lens",
        ]