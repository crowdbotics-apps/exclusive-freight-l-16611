from django.conf import settings
from django.db import models


class Category(models.Model):
    "Generated Model"
    name = models.CharField(max_length=255,)
    icon = models.URLField()
    description = models.TextField(null=True, blank=True,)
    is_recurring = models.BooleanField(null=True, blank=True,)


class Subcategory(models.Model):
    "Generated Model"
    name = models.CharField(max_length=255,)
    category = models.ForeignKey(
        "task_category.Category",
        on_delete=models.CASCADE,
        related_name="subcategory_category",
    )
    description = models.TextField(null=True, blank=True,)


# Create your models here.
