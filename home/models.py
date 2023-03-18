from django.db import models
from django.utils import timezone

from wagtail.models import Page


class HomePage(Page):
    pass


class TimeEntry(models.Model):

    class Meta:
        verbose_name_plural = 'time entries'

    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.description} ({self.start_time.strftime('%Y-%m-%d %H:%M:%S')})"
