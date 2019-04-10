from datetime import timedelta

from django import forms

from Devices.models import Device
from ServiceJobs.models import Job, Report, Event
from django.contrib.auth.models import User
from django.utils.timezone import now
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput


class UserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()


class ReportCreateForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=Job.objects.filter(isCompleted=False), label='Zlecenie')
    engineer = UserModelChoiceField(queryset=User.objects.filter(groups__name='Engineers'), label='Inżynier')

    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'startedDate': DatePickerInput(
                options={
                    'format': 'YYYY-MM-DD',
                    'maxDate': now().strftime("%Y-%m-%d"),
                    'locale': 'pl',
                }
            ),
            'finishedDate': DatePickerInput(
                options={
                    'format': 'YYYY-MM-DD',
                    'minDate': (now()-timedelta(days=2)).strftime("%Y-%m-%d"),
                    'maxDate': (now()).strftime("%Y-%m-%d"),
                    'locale': 'pl',
                }
            ),
        }


class EventCreateForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=Job.objects.filter(isCompleted=False).filter(event__isnull=True), label='Zlecenie')
    engineer = UserModelChoiceField(queryset=User.objects.filter(groups__name='Engineers'), label='Inżynier')

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'startDateTime': DateTimePickerInput(
                options={
                    'format': 'YYYY-MM-DD HH:mm',
                    'minDate': now().strftime("%Y-%m-%d %H:%M"),
                    'enabledHours': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                    'showTodayButton': True,
                    'locale': 'pl',
                }
            ),
            'endDateTime': DateTimePickerInput(
                options={
                    'format': 'YYYY-MM-DD HH:mm',
                    'minDate': now().strftime("%Y-%m-%d %H:%M"),
                    'enabledHours': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                    'showTodayButton': True,
                    'locale': 'pl',
                }
            ),
        }


class JobCreateForm(forms.ModelForm):
    device = forms.ModelChoiceField(queryset=Device.objects.all().order_by('hospital__city'), label='Urządzenie')

    class Meta:
        model = Job
        fields = ['device', 'jobType']