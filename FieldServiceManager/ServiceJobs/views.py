from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View

from ServiceJobs.forms import ReportCreateForm, EventCreateForm
from ServiceJobs.models import Job, JobType, Report, Event


class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'
    # Prioritize non completed jobs


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'


class JobCreateView(CreateView):
    model = Job
    fields = ['device', 'jobType', 'addedBy']
    # Field 'addedBy' to be replaced by currently logged user

    def get_success_url(self):
        return reverse_lazy('job-detail', kwargs={'pk': self.object.id})


class ReportListView(ListView):
    model = Report
    context_object_name = 'reports'


class ReportDetailView(DetailView):
    model = Report
    context_object_name = 'report'
    # Generating PDF of report


class ReportCreateView(CreateView):
    model = Report
    form_class = ReportCreateForm

    def get_success_url(self):
        return reverse_lazy('report-detail', kwargs={'pk': self.object.job_id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        job = Job.objects.get(pk=self.object.job.id)
        job.isCompleted = True
        job.save()
        return super().form_valid(form)


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


class CalendarView(View):
    def get(self, request):
        openJobs = Job.objects.filter(isCompleted=False)
        ctx = {
            'openJobs': openJobs
        }
        return render(request, 'ServiceJobs/main.html', ctx)


class EventListView(ListView):
    model = Event
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'


class EventCreateView(CreateView):
    model = Event
    form_class = EventCreateForm

    def get_success_url(self):
        return reverse_lazy('event-detail', kwargs={'pk': self.object.job_id})
