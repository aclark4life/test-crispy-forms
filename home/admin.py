from django.contrib import admin
from .models import TimeEntry

class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ('description', 'start_time', 'end_time')

admin.site.register(TimeEntry, TimeEntryAdmin)

