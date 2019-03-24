from django.shortcuts import render
from django.views.generic import ListView, DetailView
from ServiceJobs.models import Hospital, Device, Caretaker


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
