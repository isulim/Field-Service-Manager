from django.db import migrations

def feed_basic_data(apps, schema_editor):
    Manufacturer = apps.get_model('Devices', 'Manufacturer')
    JobType = apps.get_model('Devices', 'JobType')
    DeviceType = apps.get_model('Devices', 'DeviceType')
    Manufacturer.objects.create(name='Shimadzu')
    Manufacturer.objects.create(name='Hitachi')
    Manufacturer.objects.create(name='Siemens')
    Manufacturer.objects.create(name='GE')
    Manufacturer.objects.create(name='Philips')
    Manufacturer.objects.create(name='Fuji')
    Manufacturer.objects.create(name='Carestream')
    Manufacturer.objects.create(name='Canon')

    JobType.objects.create(name='Maintenance')
    JobType.objects.create(name='Repair')
    JobType.objects.create(name='Installation')
    JobType.objects.create(name='Expertise')

    DeviceType.objects.create(name='Radiography X-ray')
    DeviceType.objects.create(name='Fluoroscopy X-ray')
    DeviceType.objects.create(name='Mobile X-ray')
    DeviceType.objects.create(name='Mammography X-ray')
    DeviceType.objects.create(name='Angiography X-ray')
    DeviceType.objects.create(name='C-arm X-ray')
    DeviceType.objects.create(name='CT')
    DeviceType.objects.create(name='MRI')


class Migration(migrations.Migration):

    dependencies = [
        ('Devices', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(feed_basic_data),
    ]
