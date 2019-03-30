from django.urls import path
from ServiceJobs.views import JobListView, JobDetailView, \
    JobTypeListView, JobTypeDetailView, \
    ReportListView, ReportDetailView


urlpatterns = [
    path('job/', JobListView.as_view(), name='job-list'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('jobtype/', JobTypeListView, name='jobtype-list'),
    path('jobtype/<int:pk>/', JobTypeDetailView, name='jobtype-detail'),
    path('report/', ReportListView.as_view(), name='report-list'),
    path('report/<int:pk>', ReportDetailView.as_view(), name='report-detail'),
]
