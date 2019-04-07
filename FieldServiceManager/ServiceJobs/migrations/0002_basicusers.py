from django.db import migrations
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.management import create_permissions
from datetime import datetime, date


def add_group_permissions(apps, schema_editor):
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None


def basicusers(apps, schema_editor):

    hanna = User.objects.create_superuser(username='hanna', email='hanna@fsm.pl', password='hanna', last_login=datetime.now())
    hanna.first_name = 'Hanna'
    hanna.last_name = 'Annah'
    hanna.save()

    office = Group.objects.create(name='Office')
    engineers = Group.objects.create(name='Engineers')

    add_job = Permission.objects.get(codename='add_job')
    change_job = Permission.objects.get(codename='change_job')
    view_job = Permission.objects.get(codename='view_job')

    add_device = Permission.objects.get(codename='add_device')
    change_device = Permission.objects.get(codename='change_device')
    view_device = Permission.objects.get(codename='view_device')

    add_hospital = Permission.objects.get(codename='add_hospital')
    change_hospital = Permission.objects.get(codename='change_hospital')
    view_hospital = Permission.objects.get(codename='view_hospital')

    add_report = Permission.objects.get(codename='add_report')
    view_report = Permission.objects.get(codename='view_report')
    change_report = Permission.objects.get(codename='change_report')

    add_caretaker = Permission.objects.get(codename='add_caretaker')
    change_caretaker = Permission.objects.get(codename='change_caretaker')
    view_caretaker = Permission.objects.get(codename='view_caretaker')

    add_event = Permission.objects.get(codename='add_event')
    change_event = Permission.objects.get(codename='change_event')
    view_event = Permission.objects.get(codename='view_event')

    view_manufacturer = Permission.objects.get(codename='view_manufacturer')
    view_devicetype = Permission.objects.get(codename='view_devicetype')
    view_jobtype = Permission.objects.get(codename='view_jobtype')

    office.permissions.add(view_job, add_job, change_job, view_device, view_caretaker,
                           view_manufacturer, view_hospital, add_hospital, change_hospital,
                           add_report, view_report, change_report, view_devicetype, view_jobtype,
                           add_device, change_device, add_caretaker, change_caretaker,
                           add_event, change_event, view_event)
    engineers.permissions.add(view_jobtype, view_job, view_devicetype, view_device, view_report,
                              view_hospital, view_manufacturer, view_caretaker, add_report, view_event)

    igor = User.objects.create_user(username='igor', email='igor@fsm.pl', password='igor', last_login=datetime.now())
    igor.first_name = 'Igor'
    igor.last_name = 'Rogi'
    igor.groups.add(engineers)
    igor.save()

    dariusz = User.objects.create_user(username='dariusz', email='dariusz@fsm.pl', password='dariusz', last_login=datetime.now())
    dariusz.first_name = 'Dariusz'
    dariusz.last_name = 'Szuirad'
    dariusz.groups.add(engineers)
    dariusz.save()

    piotr = User.objects.create_user(username='piotr', email='piotr@fsm.pl', password='piotr', last_login=datetime.now())
    piotr.first_name = 'Piotr'
    piotr.last_name = 'Rtoip'
    piotr.groups.add(engineers)
    piotr.save()

    tomasz = User.objects.create_user(username='tomasz', email='tomasz@fsm.pl', password='tomasz', last_login=datetime.now())
    tomasz.first_name = 'Tomasz'
    tomasz.last_name = 'Szamot'
    tomasz.groups.add(engineers)
    tomasz.save()

    lukasz = User.objects.create_user(username='lukasz', email='lukasz@fsm.pl', password='lukasz', last_login=datetime.now())
    lukasz.first_name = 'Łukasz'
    lukasz.last_name = 'Szakuł'
    lukasz.groups.add(engineers)
    lukasz.save()

    zbigniew = User.objects.create_user(username='zbigniew', email='zbigniew@fsm.pl', password='zbigniew', last_login=datetime.now())
    zbigniew.first_name = 'Zbigniew'
    zbigniew.last_name = 'Weingibz'
    zbigniew.groups.add(engineers)
    zbigniew.save()

    biuro = User.objects.create_user(username='biuro', email='biuro@fsm.pl', password='biuro', last_login=datetime.now())
    biuro.first_name = 'Biuro'
    biuro.groups.add(office)
    biuro.save()

    maciej = User.objects.create_user(username='maciej', email='maciej@fsm.pl', password='maciej', last_login=datetime.now())
    maciej.first_name = 'Maciej'
    maciej.last_name = 'Jeicam'
    maciej.groups.add(office)
    maciej.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceJobs', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_group_permissions),
        migrations.RunPython(basicusers)
    ]
