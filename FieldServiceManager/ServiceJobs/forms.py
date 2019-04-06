from django import forms
from ServiceJobs.models import Job, Report
from django.contrib.auth.models import User
from datetime import date


class ReportCreateForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=Job.objects.filter(isCompleted=False))
    engineer = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Engineers'))

    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'startedDate': forms.SelectDateWidget(),
            'finishedDate': forms.SelectDateWidget(),
        }
