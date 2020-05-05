from django.conf import settings
from django.db import models


class TaskerLocation(models.Model):
    "Generated Model"
    tasker = models.OneToOneField(
        "task_profile.TaskerProfile",
        on_delete=models.CASCADE,
        related_name="taskerlocation_tasker",
    )
    latitude = models.DecimalField(max_digits=12, decimal_places=8,)
    longitude = models.DecimalField(max_digits=12, decimal_places=8,)
    last_updated = models.DateTimeField(auto_now=True,)
    address = models.TextField(null=True, blank=True,)
    zip = models.CharField(null=True, blank=True, max_length=6,)


class CustomerLocation(models.Model):
    "Generated Model"
    customer = models.OneToOneField(
        "task_profile.CustomerProfile",
        on_delete=models.CASCADE,
        related_name="customerlocation_customer",
    )
    zip = models.CharField(max_length=6,)
    country = models.CharField(max_length=50,)
    location = models.ForeignKey(
        "location.MapLocation",
        on_delete=models.CASCADE,
        related_name="customerlocation_location",
    )


class TaskLocation(models.Model):
    "Generated Model"
    location = models.ForeignKey(
        "location.MapLocation",
        on_delete=models.CASCADE,
        related_name="tasklocation_location",
    )
    address = models.TextField()
    zip = models.CharField(max_length=6,)


class MapLocation(models.Model):
    "Generated Model"
    name = models.CharField(max_length=255,)
    latitude = models.DecimalField(max_digits=12, decimal_places=8,)
    longitude = models.DecimalField(max_digits=12, decimal_places=8,)


# Create your models here.
