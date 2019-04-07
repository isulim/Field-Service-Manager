from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa')
    city = models.CharField(max_length=64, verbose_name='Miasto')
    address = models.CharField(max_length=128, verbose_name='Adres')
    phone = models.CharField(max_length=16, verbose_name='Telefon')
    email = models.EmailField(null=True, verbose_name='E-mail')

    def __str__(self):
        return "{}, {}".format(self.city, self.name)


class Device(models.Model):
    sn = models.CharField(max_length=13, verbose_name='Numer seryjny')
    manufacturer = models.ForeignKey('Manufacturer', verbose_name='Producent', on_delete=models.PROTECT)
    modelName = models.CharField(max_length=64, verbose_name='Model')
    deviceType = models.ForeignKey('DeviceType', verbose_name='Typ urządzenia', on_delete=models.PROTECT)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, verbose_name='Szpital')
    installationDate = models.DateField(verbose_name='Data instalacji')
    guaranteeDate = models.DateField(verbose_name='Data gwarancji')
    lastMaintenance = models.DateField(verbose_name='Ostatni przegląd')
    nextMaintenance = models.DateField(verbose_name='Następny przegląd')
    caretaker = models.ForeignKey('Caretaker', null=True, verbose_name='Opiekun', on_delete=models.PROTECT)

    def __str__(self):
        return "{} {}, S/N: {}".format(self.manufacturer, self.modelName, self.sn)


class Caretaker(models.Model):
    firstName = models.CharField(max_length=32, verbose_name='Imię')
    lastName = models.CharField(max_length=64, verbose_name='Nazwisko')
    hospital = models.ForeignKey('Hospital', verbose_name='Szpital', on_delete=models.CASCADE)
    phone = models.CharField(max_length=16, verbose_name='Telefon')
    email = models.EmailField(verbose_name='E-mail')

    def __str__(self):
        return "{} {}, szpital: {}".format(self.firstName, self.lastName, self.hospital)


class Manufacturer(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
