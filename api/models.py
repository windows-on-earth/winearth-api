# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Image(models.Model):
    nasa_filename = models.CharField(primary_key=True, max_length=32)
    woe_filename = models.CharField(max_length=64, blank=True, null=True)
    date_time_imported = models.DateTimeField()
    date_time_captured = models.DateTimeField(blank=True, null=True)
    nasa_expidition = models.CharField(max_length=6)
    iss_latitude = models.FloatField(blank=True, null=True)
    iss_longitude = models.FloatField(blank=True, null=True)
    iss_altitude = models.FloatField(blank=True, null=True)
    iss_velocity = models.FloatField(blank=True, null=True)
    iss_geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    iss_3d_geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_latitude = models.FloatField(blank=True, null=True)
    target_longitude = models.FloatField(blank=True, null=True)
    target_altitude = models.FloatField(blank=True, null=True)
    target_geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    exif_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    exif_processed = models.BooleanField()
    camera_fov = models.FloatField(blank=True, null=True)
    camera_orientation = models.TextField(blank=True, null=True)  # This field type is a guess.
    camera = models.TextField(blank=True, null=True)  # This field type is a guess.
    lens = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'image'
        db_table_comment = 'base repository of images'
