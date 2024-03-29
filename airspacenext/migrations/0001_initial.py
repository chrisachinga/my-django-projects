# Generated by Django 5.0.2 on 2024-02-16 20:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airline",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("code", models.CharField(blank=True, max_length=3)),
                ("icao", models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name="Airport",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("altitude", models.IntegerField()),
                ("name", models.CharField(max_length=255)),
                ("icao", models.CharField(max_length=4)),
                ("iata", models.CharField(max_length=3)),
                ("country", models.CharField(max_length=255)),
            ],
        ),
    ]
