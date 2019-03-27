from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from ServiceJobs.models import Hospital, Device, Caretaker, Manufacturer, DeviceType, JobType


class HospitalListView(ListView):
    model = Hospital
    context_object_name = 'hospitals'


class HospitalDetailView(DetailView):
    model = Hospital
    context_object_name = 'hospital'


class DeviceListView(ListView):
    model = Device
    context_object_name = 'devices'


class DeviceDetailView(DetailView):
    model = Device
    context_object_name = 'device'


class DeviceTypesList(View):
    def get(self, request):
        ctx = {'deviceTypes': DEVICE_TYPE}
        return render(request, 'ServiceJobs/device_type_list.html', ctx)


class DeviceByTypeListView(ListView):
    model = Device
    context_object_name = 'devices'
    template_name = 'ServiceJobs/device_by_type_list.html'

    def get_queryset(self):
        return Device.objects.filter(deviceType=(self.kwargs['devtype']))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deviceType'] = DEVICE_TYPE[self.kwargs['devtype']][1]
        return context


class DeviceManufacturersList(View):
    def get(self, request):
        ctx = {'deviceManufacturers': MANUFACTURERS}
        return render(request, 'ServiceJobs/device_manufacturer_list.html', ctx)


class DeviceManufacturerListView(ListView):
    model = Device
    context_object_name = 'devices'
    template_name = 'ServiceJobs/device_by_manufacturer_list.html'

    def get_queryset(self):
        return Device.objects.filter(manufacturer=(self.kwargs['manufacturer']))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deviceManufacturer'] = MANUFACTURERS[self.kwargs['manufacturer']][1]
        return context
