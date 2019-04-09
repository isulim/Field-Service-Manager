from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View

from Devices.models import Device
from ServiceJobs.forms import ReportCreateForm, EventCreateForm, JobCreateForm
from ServiceJobs.models import Job, JobType, Report, Event


# class JobListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'
    # permission_required = 'ServiceJobs.view_job'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'


# class JobDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    # permission_required = 'ServiceJobs.view_job'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'


class JobCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Job
    form_class = JobCreateForm
    permission_required = 'ServiceJobs.add_job'
    permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'

    def handle_no_permission(self):
        return render(self.request, 'ServiceJobs/403.html')

    def form_valid(self, form):
        job = form.save(commit=False)
        job.addedBy = self.request.user
        job.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('job-detail', kwargs={'pk': self.object.id})


# class ReportListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class ReportListView(ListView):
    model = Report
    context_object_name = 'reports'
    # permission_required = 'ServiceJobs.view_report'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'


# class ReportDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class ReportDetailView(DetailView):
    model = Report
    context_object_name = 'report'
    # permission_required = 'ServiceJobs.view_report'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'
    # Generating PDF of report


class ReportCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Report
    form_class = ReportCreateForm
    permission_required = 'ServiceJobs.add_report'
    permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'

    def handle_no_permission(self):
        return render(self.request, 'ServiceJobs/403.html')

    def get_initial(self):
        initial_data = super(ReportCreateView, self).get_initial()
        initial_data['job'] = Job.objects.get(pk=self.kwargs['pk'])
        return initial_data

    def get_success_url(self):
        return reverse_lazy('report-detail', kwargs={'pk': self.object.job_id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        job = Job.objects.get(pk=self.object.job.id)
        job.isCompleted = True
        job.save()
        return super().form_valid(form)


# class JobTypeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class JobTypeListView(ListView):
    model = JobType
    context_object_name = 'jobtypes'
    # permission_required = 'ServiceJobs.view_jobtype'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'


# class JobTypeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class JobTypeDetailView(DetailView):
    model = JobType
    context_object_name = 'jobtype'
    # permission_required = 'ServiceJobs.view_jobtype'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['jobs'] = Job.objects.filter(jobType__id=self.kwargs['pk'])
        return context


# class CalendarView(LoginRequiredMixin, PermissionRequiredMixin, View):
class CalendarView(View):
    # permission_required = 'ServiceJobs.view_event'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'

    def get(self, request):
        openJobs = Job.objects.filter(isCompleted=False, event__isnull=True).order_by('registeredDate')[:5]
        openEvents = Event.objects.filter(job__isCompleted=False)
        closedEvents = Event.objects.filter(job__isCompleted=True)
        ctx = {
            'openJobs': openJobs,
            'openEvents': openEvents,
            'closedEvents': closedEvents
        }
        return render(request, 'ServiceJobs/main.html', ctx)


class PersonalCalendarView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'ServiceJobs.view_event'
    permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'
    pass


# class EventListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    # permission_required = 'ServiceJobs.view_event'
    # permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'


class EventDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Event
    context_object_name = 'event'
    permission_required = 'ServiceJobs.view_event'
    permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'


class EventCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    permission_required = 'ServiceJobs.add_event'
    permission_denied_message = 'Nie masz uprawnień do wyświetlania tej strony.'
    success_url = '/'

    def handle_no_permission(self):
        return render(self.request, 'ServiceJobs/403.html')

    def get_initial(self):
        initial_data = super(EventCreateView, self).get_initial()
        initial_data['job'] = Job.objects.get(pk=self.kwargs['pk'])
        return initial_data
