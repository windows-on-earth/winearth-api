# Generated by Django 5.0.6 on 2024-06-24 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.TextField(blank=True, null=True)),
                ('iis_mission', models.TextField(blank=True, null=True)),
                ('time_stamp', models.IntegerField(blank=True, null=True)),
                ('seconds', models.IntegerField(blank=True, null=True)),
                ('images', models.IntegerField(blank=True, null=True)),
                ('start_latitude', models.FloatField(blank=True, null=True)),
                ('start_longitude', models.FloatField(blank=True, null=True)),
                ('end_latitude', models.FloatField(blank=True, null=True)),
                ('end_longitude', models.FloatField(blank=True, null=True)),
                ('model', models.TextField(blank=True, null=True)),
                ('lens', models.TextField(blank=True, null=True)),
                ('iso', models.TextField(blank=True, null=True)),
                ('shutter_speed', models.TextField(blank=True, null=True)),
                ('f_number', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
