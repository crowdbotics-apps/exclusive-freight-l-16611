from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    TaskLocationViewSet,
    CustomerLocationViewSet,
    TaskerLocationViewSet,
    MapLocationViewSet,
)

router = DefaultRouter()
router.register("taskerlocation", TaskerLocationViewSet)
router.register("customerlocation", CustomerLocationViewSet)
router.register("tasklocation", TaskLocationViewSet)
router.register("maplocation", MapLocationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
