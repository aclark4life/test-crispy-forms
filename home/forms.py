from django import forms
from .models import TimeEntry


class TimeEntryForm(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = ('description', 'start_time', 'end_time')

