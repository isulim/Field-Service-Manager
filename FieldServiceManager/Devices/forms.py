from django import forms
from Devices.models import Device, Caretaker, DeviceType, Hospital
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput


class DeviceCreateForm(forms.ModelForm):
    caretaker = forms.ModelChoiceField(required=False, queryset=Caretaker.objects.all())
    hospital = forms.ModelChoiceField(required=True, queryset=Hospital.objects.all().order_by('city'))

    class Meta:
        model = Device
        exclude = ['lastMaintenance', 'nextMaintenance']
        widgets = {
            'installationDate': DatePickerInput(
                options={
                    'format': 'YYYY-MM-DD',
                    'locale': 'pl'
                }
            ),
            'guaranteeDate': DatePickerInput(
                options={
                    'format': 'YYYY-MM-DD',
                    'locale': 'pl'
                }
            ),
        }


class DeviceUpdateForm(forms.ModelForm):
    caretaker = forms.CharField(required=False)
    manufacturer = forms.CharField(disabled=True)
    sn = forms.CharField(disabled=True)
    modelName = forms.CharField(disabled=True)
    deviceType = forms.ModelChoiceField(disabled=True, queryset=DeviceType.objects.all())

    class Meta:
        model = Device
        fields = '__all__'
        widgets = {
            'installationDate': DatePickerInput(
                options={
                    'format': 'YYYY-MM-DD',
                    'locale': 'pl'
                }
            ),
            'guaranteeDate': DatePickerInput(
                options={
                    'format': 'YYYY-MM-DD',
                    'locale': 'pl'
                }
            ),
            'lastMaintenance': DatePickerInput(
                options={
                    'format': 'YYYY-MM-DD',
                    'locale': 'pl'
                }
            ),
            'nextMaintenance': DatePickerInput(
                options={
                    'format': 'YYYY-MM-DD',
                    'locale': 'pl'
                }
            ),
        }