# -*-coding:utf-8-*-
from rest_framework import serializers
from restful.models import Poi, MapSettings


class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poi
        fields = ['id', 'name', 'ip', 'port', 'lng', 'lat', 'type', 'km', 'place', 'manufacturer', 'brand', 'model', 'username', 'password', 'direction']


class MapSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapSettings
        fields = ['id', 'mapStyle', 'centerLng', 'centerLat', 'zoom']
