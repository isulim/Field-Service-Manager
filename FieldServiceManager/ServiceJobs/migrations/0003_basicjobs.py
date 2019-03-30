from django.db import migrations
from ServiceJobs.jobs_faker import FakeJob, FakeReport

def jobtypes(apps, schema_editor):

    JobType = apps.get_model('ServiceJobs', 'JobType')

    JobType.objects.create(name='Maintenance')
    JobType.objects.create(name='Repair')
    JobType.objects.create(name='Installation')
    JobType.objects.create(name='Expertise')


def populate(apps, schema_editor):
    job = FakeJob()
    report = FakeReport()

    for i in range(100):
        job.populate()

    for i in range(50):
        report.populate()


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceJobs', '0002_basicusers'),
    ]

    operations = [
        migrations.RunPython(jobtypes),
        migrations.RunPython(populate),
    ]
