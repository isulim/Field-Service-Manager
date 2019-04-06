from django import forms
from Devices.models import Device, Caretaker, DeviceType, Hospital
from datetime import date


class DeviceCreateForm(forms.ModelForm):
    caretaker = forms.ModelChoiceField(required=False, queryset=Caretaker.objects.all())
    hospital = forms.ModelChoiceField(required=True, queryset=Hospital.objects.all().order_by('city'))

    class Meta:
        model = Device
        exclude = ['lastMaintenance', 'nextMaintenance']
        widgets = {
            'installationDate': forms.SelectDateWidget(),
            'guaranteeDate': forms.SelectDateWidget(),
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
            'installationDate': forms.SelectDateWidget(),
            'guaranteeDate': forms.SelectDateWidget(),
            'lastMaintenance': forms.SelectDateWidget(),
            'nextMaintenance': forms.SelectDateWidget(),
        }