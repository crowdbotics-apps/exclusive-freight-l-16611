from django.conf import settings
from django.db import models


class Schedule(models.Model):
    "Generated Model"
    dateTime = models.DateTimeField()
    description = models.TextField(null=True, blank=True,)
    track = models.TextField(null=True, blank=True,)
    location = models.ForeignKey(
        "event.Location",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="schedule_location",
    )


class Sponsor(models.Model):
    "Generated Model"
    name = models.TextField()
    logo_image = models.SlugField(max_length=50,)
    sponsor_level = models.TextField()
    presenter = models.BooleanField()
    website = models.URLField(null=True, blank=True,)
    location = models.ForeignKey(
        "event.Location",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="sponsor_location",
    )


class Presenter(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    title = models.CharField(max_length=256,)
    schedule = models.ForeignKey(
        "event.Schedule", on_delete=models.CASCADE, related_name="presenter_schedule",
    )


class VendorDetail(models.Model):
    "Generated Model"
    website = models.URLField()
    description = models.TextField()
    associated_name = models.TextField(null=True, blank=True,)
    vendor_id = models.ForeignKey(
        "event.Vendor",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="vendordetail_vendor_id",
    )


class Location(models.Model):
    "Generated Model"
    amenities = models.TextField(null=True, blank=True,)
    name = models.CharField(null=True, blank=True, max_length=256,)
    image = models.SlugField(null=True, blank=True, max_length=50,)


class MySchedule(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="myschedule_user",
    )
    schedule = models.ForeignKey(
        "event.Schedule",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="myschedule_schedule",
    )


class Vendor(models.Model):
    "Generated Model"
    name = models.TextField()
    logo_image = models.SlugField(null=True, blank=True, max_length=50,)
    type = models.TextField(null=True, blank=True,)
    website = models.URLField(null=True, blank=True,)
    location = models.ForeignKey(
        "event.Location",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="vendor_location",
    )
    category = models.ForeignKey(
        "event.Category",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="vendor_category",
    )


class Category(models.Model):
    "Generated Model"
    description = models.TextField()
    name = models.CharField(null=True, blank=True, max_length=256,)


class Faq(models.Model):
    "Generated Model"
    title = models.CharField(max_length=256,)
    description = models.TextField()


class Favorites(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="favorites_user",
    )
    vendor = models.ForeignKey(
        "event.Vendor",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="favorites_vendor",
    )


# Create your models here.
