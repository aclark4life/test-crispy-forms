from django import forms
from .models import TimeEntry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TimeEntryForm(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = ('description', 'start_time', 'end_time')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

