from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from ServiceJobs.models import Job, JobType, Report


class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'


class ReportListView(ListView):
    model = Report
    context_object_name = 'reports'


class ReportDetailView(DetailView):
    model = Report
    context_object_name = 'report'


class JobTypeListView(ListView):
    model = JobType
    context_object_name = 'jobtypes'


class JobTypeDetailView(DetailView):
    model = JobType
    context_object_name = 'jobtype'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['jobs'] = Job.objects.filter(jobType__id=self.kwargs['pk'])
        return context

