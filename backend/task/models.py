from django.conf import settings
from django.db import models


class Rating(models.Model):
    "Generated Model"
    tasker = models.ForeignKey(
        "task_profile.TaskerProfile",
        on_delete=models.CASCADE,
        related_name="rating_tasker",
    )
    rating = models.FloatField()
    timestamp_created = models.DateTimeField(auto_now_add=True,)
    review = models.TextField(null=True, blank=True,)
    customer = models.ForeignKey(
        "task_profile.CustomerProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rating_customer",
    )


class Message(models.Model):
    "Generated Model"
    customer = models.ForeignKey(
        "task_profile.CustomerProfile",
        on_delete=models.CASCADE,
        related_name="message_customer",
    )
    tasker = models.ForeignKey(
        "task_profile.TaskerProfile",
        on_delete=models.CASCADE,
        related_name="message_tasker",
    )
    message = models.TextField()
    timestamp_created = models.DateTimeField(auto_now_add=True,)
    task = models.ForeignKey(
        "task.Task",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="message_task",
    )


class TaskTransaction(models.Model):
    "Generated Model"
    status = models.CharField(max_length=10,)
    timestamp_completed = models.DateTimeField(null=True, blank=True,)
    task = models.ForeignKey(
        "task.Task",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="tasktransaction_task",
    )
    date = models.DateField(null=True, blank=True,)
    timestamp_started = models.DateTimeField(null=True, blank=True,)


class Task(models.Model):
    "Generated Model"
    customer = models.ForeignKey(
        "task_profile.CustomerProfile",
        on_delete=models.CASCADE,
        related_name="task_customer",
    )
    tasker = models.ForeignKey(
        "task_profile.TaskerProfile",
        on_delete=models.CASCADE,
        related_name="task_tasker",
    )
    category = models.ForeignKey(
        "task_category.Category",
        on_delete=models.CASCADE,
        related_name="task_category",
    )
    details = models.TextField()
    frequency = models.CharField(max_length=7,)
    size = models.CharField(max_length=6,)
    location = models.OneToOneField(
        "location.TaskLocation", on_delete=models.CASCADE, related_name="task_location",
    )
    is_confirmed = models.BooleanField()
    status = models.CharField(max_length=10,)
    timestamp_created = models.DateTimeField(auto_now_add=True,)
    timestamp_confirmed = models.DateTimeField(null=True, blank=True,)
    subcategory = models.ForeignKey(
        "task_category.Subcategory",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="task_subcategory",
    )


# Create your models here.
