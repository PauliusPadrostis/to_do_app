from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ['creation_datetime', 'task', 'due_date', 'status', 'user',]

    def creation_datetime(self, obj):
        return obj.creation_date.strftime('%Y-%m-%d %H:%M:%S')

    creation_datetime.short_description = 'Creation Date & Time'


# Register your models here.
admin.site.register(Task, TaskAdmin)
