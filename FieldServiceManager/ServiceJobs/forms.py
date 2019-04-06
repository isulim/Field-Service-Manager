from django import forms
from ServiceJobs.models import Job, Report, Event
from django.contrib.auth.models import User
from django.utils.timezone import now
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput

class ReportCreateForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=Job.objects.filter(isCompleted=False))
    engineer = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Engineers'))

    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'startedDate': DatePickerInput(
                options={
                    'format': 'YYYY/MM/DD',
                    'maxDate': now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            ),
            'finishedDate': DatePickerInput(
                options={
                    'format': 'YYYY/MM/DD',
                    'minDate': now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            ),
        }


class EventCreateForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=Job.objects.filter(isCompleted=False))
    engineer = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Engineers'))

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'startDateTime': DateTimePickerInput(
                options={
                    'format': 'YYYY-MM-DD HH:mm',
                    'minDate': now().strftime("%Y-%m-%d %H:%M"),
                }
            ),
            'endDateTime': DateTimePickerInput(
                options={
                    'format': 'YYYY-MM-DD HH:mm',
                    'minDate': now().strftime("%Y-%m-%d %H:%M"),
                }
            ),
        }
