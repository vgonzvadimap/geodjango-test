# Generated by Django 3.2.7 on 2021-09-23 13:57

from django.contrib.postgres.operations import CreateExtension
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PolygonPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(
                    blank=True, null=True, srid=4326)),
                ('addr_city', models.CharField(blank=True,
                 db_column='addr:city', max_length=255, null=True)),
                ('addr_street', models.CharField(blank=True,
                 db_column='addr:street', max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_phone', models.CharField(blank=True,
                 db_column='contact:phone', max_length=255, null=True)),
            ],
            options={
                'db_table': 'polygon_points',
                'managed': False,
            },
        ),
    ]