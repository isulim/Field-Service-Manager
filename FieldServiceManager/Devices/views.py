from datetime import timedelta

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View

from Devices.models import Hospital, Device, Caretaker, Manufacturer, DeviceType
from ServiceJobs.models import Job


class HospitalListView(ListView):
    model = Hospital
    context_object_name = 'hospitals'


class HospitalDetailView(DetailView):
    model = Hospital
    context_object_name = 'hospital'


class HospitalCreateView(CreateView):
    model = Hospital
    fields = '__all__'
    success_url = '/hospital/'


class DeviceListView(ListView):
    model = Device
    context_object_name = 'devices'


class DeviceDetailView(DetailView):
    model = Device
    context_object_name = 'device'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['jobs'] = Job.objects.filter(device=self.kwargs['pk'])
        return context


class DeviceCreateView(CreateView):
    model = Device
    fields = ['sn', 'manufacturer', 'modelName', 'deviceType', 'hospital',
              'installationDate', 'guaranteeDate']
    success_url = '/device/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        lastMaint = form.cleaned_data.get('installationDate')
        self.object.lastMaintenance = lastMaint
        self.object.nextMaintenance = lastMaint + timedelta(days=182)
        self.object.save()
        return super().form_valid(form)


class DeviceTypeListView(ListView):
    model = DeviceType
    context_object_name = 'deviceTypes'


class DeviceTypeDetailView(DetailView):
    model = DeviceType
    context_object_name = 'deviceType'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['devices'] = Device.objects.filter(deviceType=self.kwargs['pk'])
        return context


class ManufacturerListView(ListView):
    model = Manufacturer
    context_object_name = 'manufacturers'


class ManufacturerDetailView(DetailView):
    model = Manufacturer
    context_object_name = 'manufacturer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['devices'] = Device.objects.filter(manufacturer=self.kwargs['pk'])
        return context


class CaretakerListView(ListView):
    model = Caretaker
    context_object_name = 'caretakers'


class CaretakerDetailView(DetailView):
    model = Caretaker
    context_object_name = 'caretaker'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['devices'] = Device.objects.filter(caretaker__id=self.kwargs['pk'])
        return context
