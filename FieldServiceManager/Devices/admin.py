from django.contrib import admin
from Devices.models import Hospital, Device, DeviceType, Caretaker, Manufacturer
# Register your models here.


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['city', 'name', 'address', 'phone', 'email']


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Caretaker)
class CaretakerAdmin(admin.ModelAdmin):
    list_display = ['hospital', 'firstName', 'lastName', 'phone', 'email']


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'modelName', 'sn', 'deviceType', 'hospital', 'installationDate']

