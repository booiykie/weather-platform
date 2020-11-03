
from weather.serializers import WeatherSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse

from django_filters.rest_framework import DjangoFilterBackend

from weather.interface import Weather
# from weather import Weather, Unit

class WeatherViewSet(viewsets.ViewSet):
    """
    A simple model-less ViewSet for retrieving weather dadta.
    """

    serializer_class = WeatherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'period']

    def retrieve(self, request, city=None, period=None, *args, **kwargs):
        _city = city
        _forecast_period = period
        print(kwargs)

        weather = Weather()
        location = weather.lookup_by_location(_city, _forecast_period)
        _forecasts = location.get('main', [])

        return JsonResponse(_forecasts)