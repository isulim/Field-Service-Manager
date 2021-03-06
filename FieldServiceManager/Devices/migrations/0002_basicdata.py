from django.db import migrations
from Devices.devices_faker import FakeHospital, FakeCaretaker, FakeDevice


def basic_data(apps, schema_editor):
    Manufacturer = apps.get_model('Devices', 'Manufacturer')
    DeviceType = apps.get_model('Devices', 'DeviceType')

    Manufacturer.objects.create(name='Shimadzu')
    Manufacturer.objects.create(name='Hitachi')
    Manufacturer.objects.create(name='Siemens')
    Manufacturer.objects.create(name='GE')
    Manufacturer.objects.create(name='Philips')
    Manufacturer.objects.create(name='Fuji')
    Manufacturer.objects.create(name='Carestream')
    Manufacturer.objects.create(name='Canon')

    DeviceType.objects.create(name='RTG radiograficzny')
    DeviceType.objects.create(name='RTG fluoroskopijny')
    DeviceType.objects.create(name='RTG mobilny')
    DeviceType.objects.create(name='Mammograf')
    DeviceType.objects.create(name='Angiograf')
    DeviceType.objects.create(name='Ramię-C')
    DeviceType.objects.create(name='CT')
    DeviceType.objects.create(name='MRI')


def populate(apps, schema_editor):
    hospital = FakeHospital()
    caretaker = FakeCaretaker()
    device = FakeDevice()
    for i in range(5):
        hospital.populate()
    for i in range(10):
        caretaker.populate()
    for i in range(20):
        device.populate()


class Migration(migrations.Migration):

    dependencies = [
        ('Devices', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(basic_data),
        migrations.RunPython(populate),
    ]
