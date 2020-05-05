from django.conf import settings
from django.db import models


class InviteCode(models.Model):
    "Generated Model"
    code = models.CharField(max_length=20,)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="invitecode_user",
    )
    timestamp_created = models.DateTimeField(auto_now_add=True,)


class TaskerProfile(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="taskerprofile_user",
    )
    mobile_number = models.CharField(max_length=20,)
    photo = models.URLField()
    timestamp_created = models.DateTimeField(auto_now_add=True,)
    last_updated = models.DateTimeField(auto_now=True,)
    last_login = models.DateTimeField(null=True, blank=True,)
    description = models.TextField(null=True, blank=True,)
    city = models.CharField(null=True, blank=True, max_length=50,)
    vehicle = models.CharField(null=True, blank=True, max_length=50,)
    closing_message = models.TextField(null=True, blank=True,)
    work_area_radius = models.FloatField(null=True, blank=True,)


class CustomerProfile(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="customerprofile_user",
    )
    mobile_number = models.CharField(max_length=20,)
    photo = models.URLField()
    timestamp_created = models.DateTimeField(auto_now_add=True,)
    last_updated = models.DateTimeField(auto_now=True,)
    last_login = models.DateTimeField(null=True, blank=True,)


class Notification(models.Model):
    "Generated Model"
    type = models.CharField(max_length=20,)
    message = models.TextField()
    user = models.ManyToManyField("users.User", related_name="notification_user",)
    timestamp_created = models.DateTimeField(auto_now_add=True,)


# Create your models here.
