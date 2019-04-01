from django import forms
from Devices.models import Device, Caretaker, DeviceType
from datetime import date


class DeviceCreateForm(forms.ModelForm):
    caretaker = forms.ModelChoiceField(required=False, queryset=Caretaker.objects.all())

    class Meta:
        model = Device
        exclude = ['lastMaintenance', 'nextMaintenance']
        widgets = {
            'installationDate': forms.SelectDateWidget(years=range(2010, (date.today().year + 1))),
            'guaranteeDate': forms.SelectDateWidget(years=range(2010, (date.today().year + 10))),
        }


class DeviceUpdateForm(forms.ModelForm):
    caretaker = forms.ModelChoiceField(required=False, queryset=Caretaker.objects.all())
    manufacturer = forms.CharField(disabled=True)
    sn = forms.CharField(disabled=True)
    modelName = forms.CharField(disabled=True)
    deviceType = forms.ModelChoiceField(disabled=True, queryset=DeviceType.objects.all())

    class Meta:
        model = Device
        fields = '__all__'
        widgets = {
            'installationDate': forms.SelectDateWidget(years=range(2010, (date.today().year + 1))),
            'guaranteeDate': forms.SelectDateWidget(years=range(2010, (date.today().year + 10))),
            'lastMaintenance': forms.SelectDateWidget(years=range(2010, (date.today().year + 10))),
            'nextMaintenance': forms.SelectDateWidget(years=range(2010, (date.today().year + 10))),
        }