import uuid
from django.db import models


class Airport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.IntegerField()
    name = models.CharField(max_length=255)
    icao = models.CharField(max_length=4)
    iata = models.CharField(max_length=3)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Airline(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, blank=True)
    icao = models.CharField(max_length=4)

    def __str__(self):
        return self.name
