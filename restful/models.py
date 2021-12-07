from django.db import models


# Create your models here.
class Poi(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    port = models.IntegerField(default=80)
    lng = models.DecimalField(decimal_places=10, max_digits=13)
    lat = models.DecimalField(decimal_places=10, max_digits=13)
    type = models.CharField(max_length=20, null=True, blank=False)
    km = models.DecimalField(decimal_places=3, max_digits=7, null=True, blank=False)
    place = models.CharField(max_length=20, null=True, blank=False)
    manufacturer = models.CharField(max_length=80, null=True, blank=True)
    brand = models.CharField(max_length=20, blank=True)
    model = models.CharField(max_length=20, blank=True)
    username = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, blank=True)
    direction = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class MapSettings(models.Model):
    id = models.AutoField(primary_key=True)
    mapStyle = models.CharField(max_length=100)
    centerLng = models.DecimalField(decimal_places=10, max_digits=13, blank=False, default=0)
    centerLat = models.DecimalField(decimal_places=10, max_digits=13, blank=False, default=0)
    zoom = models.IntegerField()

    class Meta:
        ordering = ['id']
