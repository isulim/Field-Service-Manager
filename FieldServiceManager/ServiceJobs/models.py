from django.db import models
from django.contrib.auth.models import User

MANUFACTURERS = (
    (1, 'SHIMADZU'),
    (2, "HITACHI"),
    (3, 'SIEMENS'),
    (4, 'PHILIPS'),
    (5, 'GENERAL ELECTRIC'),
    (6, 'CANON'),
    (7, 'FUJI'),
    (8, 'CARESTREAM'),
    (9, 'OTHER'),
)

DEVICE_TYPE = (
    (1, 'Radiography X-Ray'),
    (2, 'Fluoroscope X-Ray'),
    (3, 'Angiography X-Ray'),
    (4, 'Mobile X-Ray'),
    (5, 'CT'),
    (6, 'MRI'),
    (7, 'USG'),
    (8, 'PET'),
    (9, 'SPECT'),
    (10, 'PET-CT'),
    (11, 'PET-MR'),
    (12, 'SPECT-CT'),
)

JOB_TYPE = (
    (1, 'Maintenance'),
    (2, 'Repair'),
    (3, 'Installation'),
    (4, 'Expertise'),
)


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
    deviceType = models.SmallIntegerField(choices=DEVICE_TYPE, verbose_name='Device type')
    manufacturer = models.SmallIntegerField(choices=MANUFACTURERS, verbose_name='Manufacturer')
    modelName = models.CharField(max_length=64, verbose_name='Model')
    installation = models.DateField(verbose_name='Installation date')
    guaranteeDate = models.DateField(verbose_name='Guarantee date')
    lastMaintenance = models.DateField(verbose_name='Last maintenance')
    nextMaintenance = models.DateField(verbose_name='Next maintenance')
    caretaker = models.ForeignKey('Caretaker', verbose_name='Caretaker', on_delete=models.PROTECT)

    def __str__(self):
        return "{}, {}, S/N: {}".format(self.manufacturer, self.modelName, self.sn)


class Job(models.Model):
    device = models.ForeignKey('Device', on_delete=models.CASCADE, verbose_name='Device')
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, verbose_name='Hospital')
    jobType = models.SmallIntegerField(choices=JOB_TYPE, verbose_name='Job type')
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
