from django.conf import settings
from django.db import models


class TaskerSkill(models.Model):
    "Generated Model"
    tasker = models.ForeignKey(
        "task_profile.TaskerProfile",
        on_delete=models.CASCADE,
        related_name="taskerskill_tasker",
    )
    name = models.CharField(max_length=255,)
    rate = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(
        "task_category.Category",
        on_delete=models.CASCADE,
        related_name="taskerskill_category",
    )
    subcategory = models.ForeignKey(
        "task_category.Subcategory",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="taskerskill_subcategory",
    )


class BusinessPhoto(models.Model):
    "Generated Model"
    tasker = models.ForeignKey(
        "task_profile.TaskerProfile",
        on_delete=models.CASCADE,
        related_name="businessphoto_tasker",
    )
    photo = models.URLField()
    description = models.TextField()


class TaskerAvailability(models.Model):
    "Generated Model"
    tasker = models.OneToOneField(
        "task_profile.TaskerProfile",
        on_delete=models.CASCADE,
        related_name="taskeravailability_tasker",
    )
    timeslots = models.ManyToManyField(
        "tasker_business.Timeslot", related_name="taskeravailability_timeslots",
    )


class Timeslot(models.Model):
    "Generated Model"
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


# Create your models here.
