from django import forms
from .models import TimeEntry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Div, Field, Submit
from django.forms.widgets import DateTimeInput
from django.utils import timezone


class TimeEntryForm(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = ('description', 'start_time', 'end_time')

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-inline'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.layout = Div(
            Div(Field('start_time', css_class='form-control'), css_class='col-sm-6'),
            Div(Field('end_time', css_class='form-control'), css_class='col-sm-6'),
            Div(Field('description', css_class='form-control'), css_class='col-sm-12'),
            css_class='row'
        )

    start_time = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}), initial=timezone.datetime.now() )
    end_time = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}), initial=timezone.datetime.now() + timezone.timedelta(hours=1))

