from django.db import models
from django.contrib.auth.models import User


class Hospital(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name')
    city = models.CharField(max_length=64, verbose_name='City')
    address = models.CharField(max_length=128, verbose_name='Address')
    phone = models.CharField(max_length=16, verbose_name='Phone')
    email = models.EmailField(null=True, verbose_name='E-mail')

    def __str__(self):
        return "{}, {}".format(self.name, self.city)


class Device(models.Model):
    sn = models.CharField(primary_key=True, max_length=13, verbose_name='Serial number')
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, verbose_name='Hospital')
    deviceType = models.ForeignKey('DeviceType', verbose_name='Device type', on_delete=models.PROTECT)
    manufacturer = models.ForeignKey('Manufacturer', verbose_name='Manufacturer', on_delete=models.PROTECT)
    modelName = models.CharField(max_length=64, verbose_name='Model')
    installation = models.DateField(verbose_name='Installation date')
    guaranteeDate = models.DateField(verbose_name='Guarantee date')
    lastMaintenance = models.DateField(verbose_name='Last maintenance')
    nextMaintenance = models.DateField(verbose_name='Next maintenance')
    caretaker = models.ForeignKey('Caretaker', verbose_name='Caretaker', on_delete=models.PROTECT)

    def __str__(self):
        return "{}, model: {}, S/N: {}".format(self.manufacturer, self.modelName, self.sn)


class Job(models.Model):
    device = models.ForeignKey('Device', on_delete=models.CASCADE, verbose_name='Device')
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, verbose_name='Hospital')
    jobType = models.ForeignKey('JobType', verbose_name='Job type', on_delete=models.PROTECT)
    registered = models.DateField(verbose_name='Registered date', auto_now_add=True)
    scheduled = models.DateField(verbose_name='Scheduled date')
    isCompleted = models.BooleanField(default=False, verbose_name='Completed')

    def __str__(self):
        return "{} - {}, {}".format(self.jobType, self.device, self.hospital)


class Report(models.Model):
    job = models.OneToOneField('Job', on_delete=models.CASCADE, verbose_name='Job', primary_key=True)
    engineer = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Engineer')
    started = models.DateField(verbose_name='Started date')
    finished = models.DateField(verbose_name='Finished date')
    workHours = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return "{}: {} - {}".format(self.job, self.engineer, self.finished)


class Caretaker(models.Model):
    firstName = models.CharField(max_length=32, verbose_name='First name')
    lastName = models.CharField(max_length=64, verbose_name='Last name')
    hospital = models.ForeignKey('Hospital', verbose_name='Hospital', on_delete=models.CASCADE)
    phone = models.CharField(max_length=16, verbose_name='Phone')
    email = models.EmailField(verbose_name='E-mail')

    def __str__(self):
        return "{} {}, {}".format(self.firstName, self.lastName, self.hospital)


class Manufacturer(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class JobType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
