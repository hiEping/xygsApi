# Create your views here.
from rest_framework import viewsets
from restful.models import Poi, MapSettings
from restful.serializers import PoiSerializer, MapSettingsSerializer


class PoiViewSet(viewsets.ModelViewSet):
    queryset = Poi.objects.all()
    serializer_class = PoiSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        # ip = self.request.query_params.get('ip')
        # port = self.request.query_params.get('port')
        # lng = self.request.query_params.get('lng')
        # lat = self.request.query_params.get('lat')
        type = self.request.query_params.get('type')
        # km = self.request.query_params.get('km')
        place = self.request.query_params.get('place')
        manufacturer = self.request.query_params.get('manufacturer')
        brand = self.request.query_params.get('brand')
        model = self.request.query_params.get('model')
        # username = self.request.query_params.get('username')
        # password = self.request.query_params.get('password')
        direction = self.request.query_params.get('direction')

        if name is not None:
            self.queryset = self.queryset.filter(name__contains=name)
        if type is not None and type != 'all':
            self.queryset = self.queryset.filter(type=type)
        if place is not None and place != 'all':
            self.queryset = self.queryset.filter(place=place)
        if direction is not None and direction != 'all':
            self.queryset = self.queryset.filter(direction=direction)
        return self.queryset


class MapSettingsViewSet(viewsets.ModelViewSet):
    queryset = MapSettings.objects.all()
    serializer_class = MapSettingsSerializer
