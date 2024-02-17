from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Airport, Airline


@admin.register(Airport)
class AirportAdmin(ImportExportModelAdmin):
    list_display = ("name", "icao", "iata", "country")
    list_filter = ("country",)
    search_fields = ("name", "icao", "iata", "country")


@admin.register(Airline)
class AirlineAdmin(ImportExportModelAdmin):
    list_display = ("name", "code", "icao")
    search_fields = ("name", "code", "icao")
