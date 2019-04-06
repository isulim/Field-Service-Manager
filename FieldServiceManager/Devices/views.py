from datetime import timedelta

from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.base import View

from Devices.models import Hospital, Device, Caretaker, Manufacturer, DeviceType
from ServiceJobs.models import Job
from Devices.forms import DeviceCreateForm, DeviceUpdateForm


class HospitalListView(ListView):
    model = Hospital
    context_object_name = 'hospitals'
    queryset = Hospital.objects.all().order_by('city')


class HospitalDetailView(DetailView):
    model = Hospital
    context_object_name = 'hospital'


class HospitalCreateView(CreateView):
    model = Hospital
    fields = '__all__'
    success_url = '/hospital/'


class HospitalUpdateView(UpdateView):
    model = Hospital
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('hospital-detail', kwargs={'pk': self.object.id})


class DeviceListView(ListView):
    model = Device
    context_object_name = 'devices'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['shimadzu'] = Device.objects.filter(manufacturer=1)
        context['hitachi'] = Device.objects.filter(manufacturer=2)
        context['siemens'] = Device.objects.filter(manufacturer=3)
        context['ge'] = Device.objects.filter(manufacturer=4)
        context['philips'] = Device.objects.filter(manufacturer=5)
        context['fuji'] = Device.objects.filter(manufacturer=6)
        context['carestream'] = Device.objects.filter(manufacturer=7)
        context['canon'] = Device.objects.filter(manufacturer=8)
        return context


class DeviceDetailView(DetailView):
    model = Device
    context_object_name = 'device'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['jobs'] = Job.objects.filter(device=self.kwargs['pk'])
        return context


class DeviceCreateView(CreateView):
    model = Device
    form_class = DeviceCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        lastMaint = form.cleaned_data.get('installationDate')
        self.object.lastMaintenance = lastMaint
        self.object.nextMaintenance = lastMaint + timedelta(days=182)
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('device-detail', kwargs={'pk': self.object.id})

# One update for office, other for full permissions?
class DeviceUpdateView(UpdateView):
    model = Device
    form_class = DeviceUpdateForm

    def get_success_url(self):
        return reverse_lazy('device-detail', kwargs={'pk': self.object.id})


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


class CaretakerCreateView(CreateView):
    model = Caretaker
    fields = '__all__'
    success_url = '/caretaker/'

    def get_success_url(self):
        return reverse_lazy('caretaker-detail', kwargs={'pk': self.object.id})


class CaretakerUpdateView(UpdateView):
    model = Caretaker
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('caretaker-detail', kwargs={'pk': self.object.id})

