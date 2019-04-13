from django.contrib import admin
from ServiceJobs.models import Event, JobType, Job, Report
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['job', 'engineer', 'startDateTime', 'endDateTime']


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['registeredDate', 'jobType', 'addedBy', 'device', 'isCompleted']


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['job', 'startedDate', 'finishedDate', 'engineer', 'workHours']


admin.site.site_header = 'Field Service Manager'
admin.site.site_title = 'Field Service Manager - panel administracyjny'
admin.site.index_title = 'Zarządzanie aplikacją'
