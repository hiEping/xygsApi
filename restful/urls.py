# -*-coding:utf-8-*-
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from restful import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pois', views.PoiViewSet)
router.register(r'mapSettings', views.MapSettingsViewSet)

urlpatterns = [
    path('openapi/', get_schema_view(
        title="xygs api",
        description="API for Poi , MapSettings …",
        version="0.2.0"
    ), name='openapi-schema'),
    path('', include(router.urls)),
]
