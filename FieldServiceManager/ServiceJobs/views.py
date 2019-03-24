from django.shortcuts import render
from django.views.generic import ListView, DetailView
from ServiceJobs.models import Hospital, Device, Caretaker


class HospitalListView(ListView):
    model = Hospital
    context_object_name = 'hospitals'


class HospitalDetailView(DetailView):
    model = Hospital
    context_object_name = 'hospital'
