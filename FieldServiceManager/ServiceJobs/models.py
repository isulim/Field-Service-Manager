from django.db import models
from django.contrib.auth.models import User
from Devices.models import Device, Hospital
from django.utils.timezone import now


class JobType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Job(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='Device')
    jobType = models.ForeignKey(JobType, verbose_name='Job type', on_delete=models.PROTECT)
    registeredDate = models.DateField(verbose_name='Registered date', auto_now_add=True)
    addedBy = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Added by')
    isCompleted = models.BooleanField(default=False, verbose_name='Completed')

    def __str__(self):
        return "{} - {}: {} {}".format(self.jobType, self.device.hospital, self.device.manufacturer, self.device.modelName)


class Report(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, verbose_name='Job', primary_key=True)
    engineer = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Engineer')
    startedDate = models.DateField(verbose_name='Started date', default=now)
    finishedDate = models.DateField(verbose_name='Finished date', default=now)
    workHours = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return "{}: {} - {}".format(self.finishedDate, self.job, self.engineer)


class Event(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, verbose_name='Job', primary_key=True)
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Engineer')
    startDateTime = models.DateTimeField(verbose_name='Start')
    endDateTime = models.DateTimeField(verbose_name='End')

    def __str__(self):
        return "{}, {}".format(self.job, self.startDateTime.date())
