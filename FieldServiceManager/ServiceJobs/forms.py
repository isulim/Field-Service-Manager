from django import forms
from ServiceJobs.models import Job, Report, Event
from django.contrib.auth.models import User
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput


class ReportCreateForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=Job.objects.filter(isCompleted=False))
    engineer = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Engineers'))

    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'startedDate': DatePickerInput(format='%Y-%m-%d'),
            'finishedDate': DatePickerInput(format='%Y-%m-%d'),
        }


class EventCreateForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=Job.objects.filter(isCompleted=False))
    engineer = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Engineers'))

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'startDateTime': DateTimePickerInput(format='%Y-%m-%d hh:mm'),
            'endDateTime': DateTimePickerInput(format='%Y-%m-%d hh:mm'),
        }
