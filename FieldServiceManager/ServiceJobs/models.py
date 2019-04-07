from django.db import models
from django.contrib.auth.models import User
from Devices.models import Device, Hospital
from django.utils.timezone import now


class JobType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Job(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='Urządzenie')
    jobType = models.ForeignKey(JobType, verbose_name='Rodzaj zlecenia', on_delete=models.PROTECT)
    registeredDate = models.DateField(verbose_name='Data zarejestowania', auto_now_add=True)
    addedBy = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Dodane przez')
    isCompleted = models.BooleanField(default=False, verbose_name='Ukończone')

    def __str__(self):
        return "{} - {}: {} {}".format(self.jobType, self.device.hospital, self.device.manufacturer, self.device.modelName)


class Report(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, verbose_name='Zlecenie', primary_key=True)
    engineer = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Inżynier')
    startedDate = models.DateField(verbose_name='Data rozpoczęcia', default=now)
    finishedDate = models.DateField(verbose_name='Data zakończenia', default=now)
    workHours = models.PositiveSmallIntegerField(verbose_name='Godziny pracy')
    description = models.TextField(verbose_name='Opis')

    def __str__(self):
        return "{}: {} - {}".format(self.finishedDate, self.job, self.engineer)


class Event(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, verbose_name='Zlecenie', primary_key=True)
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Inżynier')
    startDateTime = models.DateTimeField(verbose_name='Początek')
    endDateTime = models.DateTimeField(verbose_name='Koniec')

    def __str__(self):
        return "{}, {}".format(self.job, self.startDateTime.date())
