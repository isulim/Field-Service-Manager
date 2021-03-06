from django.urls import path
from ServiceJobs.views import JobListView, JobDetailView, \
    JobTypeListView, JobTypeDetailView, \
    ReportListView, ReportDetailView, JobCreateView, ReportCreateView, CalendarView, EventListView, \
    EventDetailView, EventCreateView, JobIdCreateView, MyPDFView


urlpatterns = [
    path('', CalendarView.as_view(), name='main'),
    path('job/', JobListView.as_view(), name='job-list'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('job/create/', JobCreateView.as_view(), name='job-create'),
    path('job/create/<int:pk>', JobIdCreateView.as_view(), name='job-create-id'),
    path('jobtype/', JobTypeListView.as_view(), name='jobtype-list'),
    path('jobtype/<int:pk>/', JobTypeDetailView.as_view(), name='jobtype-detail'),
    path('report/', ReportListView.as_view(), name='report-list'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('report/create/<int:pk>', ReportCreateView.as_view(), name='report-create-id'),
    path('event/', EventListView.as_view(), name='event-list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/create/<int:pk>', EventCreateView.as_view(), name='event-create-id'),
    path('pdf/<int:pk>/', MyPDFView.as_view(), name='pdf'),
]
