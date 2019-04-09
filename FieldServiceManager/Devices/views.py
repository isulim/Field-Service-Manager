from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from Devices.models import Hospital, Device, Caretaker, Manufacturer, DeviceType
from ServiceJobs.models import Job
from Devices.forms import DeviceCreateForm, DeviceUpdateForm


# class HospitalListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class HospitalListView(ListView):
    model = Hospital
    context_object_name = 'hospitals'
    # permission_required = 'Devices.view_hospital'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'
    queryset = Hospital.objects.all().order_by('city')


# class HospitalDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class HospitalDetailView(DetailView):
    model = Hospital
    context_object_name = 'hospital'
    # permission_required = 'Devices.view_hospital'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'


class HospitalCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Hospital
    fields = '__all__'
    success_url = '/hospital/'
    permission_required = 'Devices.add_hospital'
    permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'

    def handle_no_permission(self):
        return render(self.request, 'ServiceJobs/403.html')


class HospitalUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Hospital
    fields = '__all__'
    permission_required = 'Devices.change_hospital'
    permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'

    def get_success_url(self):
        return reverse_lazy('hospital-detail', kwargs={'pk': self.object.id})


# class DeviceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class DeviceListView(ListView):
    model = Device
    context_object_name = 'devices'
    # permission_required = 'Devices.view_device'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'

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


# class DeviceDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class DeviceDetailView(DetailView):
    model = Device
    context_object_name = 'device'
    # permission_required = 'Devices.view_device'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['jobs'] = Job.objects.filter(device=self.kwargs['pk'])
        return context


class DeviceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Device
    form_class = DeviceCreateForm
    permission_required = 'Devices.add_device'
    permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'

    def handle_no_permission(self):
        return render(self.request, 'ServiceJobs/403.html')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        lastMaint = form.cleaned_data.get('installationDate')
        self.object.lastMaintenance = lastMaint
        self.object.nextMaintenance = lastMaint + timedelta(days=182)
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('device-detail', kwargs={'pk': self.object.id})


class DeviceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Device
    form_class = DeviceUpdateForm
    permission_required = 'Devices.change_device'
    permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'

    def handle_no_permission(self):
        return render(self.request, 'ServiceJobs/403.html')

    def get_success_url(self):
        return reverse_lazy('device-detail', kwargs={'pk': self.object.id})


# class DeviceTypeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class DeviceTypeListView(ListView):
    model = DeviceType
    context_object_name = 'deviceTypes'
    # permission_required = 'Devices.view_devicetype'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'


# class DeviceTypeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class DeviceTypeDetailView(DetailView):
    model = DeviceType
    context_object_name = 'deviceType'
    # permission_required = 'Devices.view_devicetype'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['devices'] = Device.objects.filter(deviceType=self.kwargs['pk'])
        return context


# class ManufacturerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class ManufacturerListView(ListView):
    model = Manufacturer
    context_object_name = 'manufacturers'
    # permission_required = 'Devices.view_manufacturer'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'


# class ManufacturerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class ManufacturerDetailView(DetailView):
    model = Manufacturer
    context_object_name = 'manufacturer'
    # permission_required = 'Devices.view_manufacturer'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['devices'] = Device.objects.filter(manufacturer=self.kwargs['pk'])
        return context


# class CaretakerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class CaretakerListView(ListView):
    model = Caretaker
    context_object_name = 'caretakers'
    # permission_required = 'Devices.view_caretaker'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'


# class CaretakerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class CaretakerDetailView(DetailView):
    model = Caretaker
    context_object_name = 'caretaker'
    # permission_required = 'Devices.view_caretaker'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['devices'] = Device.objects.filter(caretaker__id=self.kwargs['pk'])
        return context


class CaretakerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Caretaker
    fields = '__all__'
    success_url = '/caretaker/'
    permission_required = 'Devices.add_caretaker'
    permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'

    def handle_no_permission(self):
        return render(self.request, 'ServiceJobs/403.html')

    def get_success_url(self):
        return reverse_lazy('caretaker-detail', kwargs={'pk': self.object.id})


class CaretakerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Caretaker
    fields = '__all__'
    permission_required = 'Devices.change_caretaker'
    permission_denied_message = 'Nie masz uprawnień do wyświetlenia tej strony.'

    def handle_no_permission(self):
        return render(self.request, 'ServiceJobs/403.html')

    def get_success_url(self):
        return reverse_lazy('caretaker-detail', kwargs={'pk': self.object.id})

