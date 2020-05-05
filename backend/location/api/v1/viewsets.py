from rest_framework import authentication
from location.models import TaskLocation, CustomerLocation, TaskerLocation, MapLocation
from .serializers import (
    TaskLocationSerializer,
    CustomerLocationSerializer,
    TaskerLocationSerializer,
    MapLocationSerializer,
)
from rest_framework import viewsets


class TaskerLocationViewSet(viewsets.ModelViewSet):
    serializer_class = TaskerLocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskerLocation.objects.all()


class CustomerLocationViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerLocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CustomerLocation.objects.all()


class TaskLocationViewSet(viewsets.ModelViewSet):
    serializer_class = TaskLocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskLocation.objects.all()


class MapLocationViewSet(viewsets.ModelViewSet):
    serializer_class = MapLocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = MapLocation.objects.all()
