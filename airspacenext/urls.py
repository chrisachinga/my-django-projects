from django.urls import path
from .views import home, airline_list, airport_list, airports_map

urlpatterns = [
    path("", home, name="home"),
    path("airports/", airport_list, name="airport_list"),
    path("airlines/", airline_list, name="airline_list"),
    path('airports/map/', airports_map, name='airports_map'),
]
