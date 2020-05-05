from django.contrib import admin
from .models import Task, Message, TaskTransaction, Rating

admin.site.register(Rating)
admin.site.register(Message)
admin.site.register(TaskTransaction)
admin.site.register(Task)

# Register your models here.
