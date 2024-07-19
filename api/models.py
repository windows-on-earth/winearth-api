# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movies(models.Model):
    movie = models.TextField(blank=True, null=True)
    iis_mission = models.TextField(blank=True, null=True)
    time_stamp = models.IntegerField(blank=True, null=True)
    seconds = models.IntegerField(blank=True, null=True)
    images = models.IntegerField(blank=True, null=True)
    start_latitude = models.FloatField(blank=True, null=True)
    start_longitude = models.FloatField(blank=True, null=True)
    end_latitude = models.FloatField(blank=True, null=True)
    end_longitude = models.FloatField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    lens = models.TextField(blank=True, null=True)
    iso = models.TextField(blank=True, null=True)
    shutter_speed = models.TextField(blank=True, null=True)
    f_number = models.TextField(blank=True, null=True)

    @property
    def url(self):
        return "https://windows-on-earth.sdsc.osn.xsede.org/movies/%s/%s.mp4" % (
            self.movie,
            self.movie,
        )

    @property
    def url_rt(self):
        return "https://windows-on-earth.sdsc.osn.xsede.org/movies/%s/%s-rt.mp4" % (
            self.movie,
            self.movie,
        )

    @property
    def thumbnail_512(self):
        return (
            "https://windows-on-earth.sdsc.osn.xsede.org/movies/%s/%s_thumbnail_512.webp"
            % (
                self.movie,
                self.movie,
            )
        )
