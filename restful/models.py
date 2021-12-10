from django.db import models


# Create your models here.
class Poi(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    ip = models.GenericIPAddressField(default='0.0.0.0')
    port = models.IntegerField(default=80)
    lng = models.DecimalField(decimal_places=10, max_digits=13, default=0.000001)
    lat = models.DecimalField(decimal_places=10, max_digits=13, default=0.000001)
    type = models.CharField(max_length=20, default='unknown')
    km = models.DecimalField(decimal_places=3, max_digits=7, default=0.000)
    place = models.CharField(max_length=20, default='unknown')
    manufacturer = models.CharField(max_length=80, null=True, blank=True)
    brand = models.CharField(max_length=20, null=True, blank=True)
    model = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, blank=True)
    direction = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class MapSettings(models.Model):
    id = models.AutoField(primary_key=True)
    mapStyle = models.CharField(max_length=100, default='')
    centerLng = models.DecimalField(decimal_places=10, max_digits=13, default=0.000001)
    centerLat = models.DecimalField(decimal_places=10, max_digits=13, default=0.000001)
    zoom = models.IntegerField(default=10)

    class Meta:
        ordering = ['id']
