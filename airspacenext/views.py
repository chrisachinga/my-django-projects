from django.shortcuts import render
from .models import Airport, Airline


def home(request):
    airport_count = Airport.objects.count()
    airline_count = Airline.objects.count()

    # get random 10 airports and airlines
    airports = Airport.objects.all().order_by("?")[:10]
    airlines = Airline.objects.all().order_by("?")[:10]

    context = {
        "airport_count": airport_count,
        "airline_count": airline_count,
        "airports": airports,
        "airlines": airlines,
    }
    return render(request, "airspacenext/index.html", context)


def airport_list(request):
    airports = Airport.objects.all()
    context = {"airports": airports}
    return render(request, "airspacenext/airport_list.html", context)


def airline_list(request):
    airlines = Airline.objects.all()
    context = {"airlines": airlines}
    return render(request, "airspacenext/airline_list.html", context)


def airports_map(request):
    airports = Airport.objects.all()
    context = {'airports': airports}
    return render(request, 'airspacenext/airports_map.html', context)