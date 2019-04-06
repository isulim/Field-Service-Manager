from django.urls import path
from ServiceJobs.views import JobListView, JobDetailView, \
    JobTypeListView, JobTypeDetailView, \
    ReportListView, ReportDetailView, JobCreateView, ReportCreateView, CalendarView

urlpatterns = [
    path('job/', JobListView.as_view(), name='job-list'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('job/create/', JobCreateView.as_view(), name='job-create'),
    path('jobtype/', JobTypeListView.as_view(), name='jobtype-list'),
    path('jobtype/<int:pk>/', JobTypeDetailView.as_view(), name='jobtype-detail'),
    path('report/', ReportListView.as_view(), name='report-list'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('report/create/', ReportCreateView.as_view(), name='report-create'),
    path('', CalendarView.as_view(), name='main'),
]
