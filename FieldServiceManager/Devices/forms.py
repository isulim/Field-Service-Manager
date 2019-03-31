from django import forms
from Devices.models import Device
from datetime import date

class DeviceCreateForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = ['lastMaintenance', 'nextMaintenance', 'caretaker']
        widgets = {
            'installationDate': forms.SelectDateWidget(years=range(2010, (date.today().year + 1))),
            'guaranteeDate': forms.SelectDateWidget(years=range(2010, (date.today().year + 10))),
        }
