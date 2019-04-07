from django.db import migrations
from ServiceJobs.jobs_faker import FakeJob, FakeReport

def jobtypes(apps, schema_editor):

    JobType = apps.get_model('ServiceJobs', 'JobType')

    JobType.objects.create(name='Przegląd')
    JobType.objects.create(name='Naprawa')
    JobType.objects.create(name='Instalacja')
    JobType.objects.create(name='Ekspertyza')


def populate(apps, schema_editor):
    job = FakeJob()
    report = FakeReport()

    for i in range(20):
        job.populate()

    for i in range(10):
        report.populate()


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceJobs', '0002_basicusers'),
    ]

    operations = [
        migrations.RunPython(jobtypes),
        migrations.RunPython(populate),
    ]
