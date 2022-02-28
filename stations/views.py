from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_namber = int(request.GET.get("page", 1))
    with open('data-398-2018-08-30.csv', 'r', encoding='UTF-8') as csvfile:
        stations = csv.DictReader(csvfile)
        bus_station = []
        for station in stations:
            bus_station.append(station)
    paginator = Paginator(bus_station, 10)
    page = paginator.get_page(page_namber)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
