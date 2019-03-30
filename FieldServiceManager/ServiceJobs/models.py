from django.db import models
from django.contrib.auth.models import User
from Devices.models import Device, Hospital


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
        return "{} - {}, {}".format(self.jobType, self.device, self.device.hospital)


class Report(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, verbose_name='Job', primary_key=True)
    engineer = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Engineer')
    started = models.DateField(verbose_name='Started date')
    finished = models.DateField(verbose_name='Finished date')
    workHours = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return "{}: {} - {}".format(self.job, self.engineer, self.finished)
