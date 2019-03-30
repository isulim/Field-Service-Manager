from faker import Faker
from datetime import timedelta
from random import randint, choice, getrandbits
from django.contrib.auth.models import User
from ServiceJobs.models import Job, JobType, Report
from Devices.models import Device


class FakeJob:
    faker = Faker('pl_PL')

    def populate(self):
        """Create fake service job"""
        devices = Device.objects.all()
        jobtypes = JobType.objects.all()
        job = Job()
        job.device = choice(devices)
        job.jobType = choice(jobtypes)
        job.addedBy = User.objects.get(username='hanna')
        job.isCompleted = bool(getrandbits(1))
        job.save()
        print(job)


class FakeReport:
    faker = Faker('pl_PL')

    def populate(self):
        """Create fake report related to a job."""
        jobs = Job.objects.filter(isCompleted=True)
        enginners = User.objects.filter(groups__name='Engineers')
        report = Report()
        report.job = choice(jobs)
        report.engineer = choice(enginners)
        start_date = self.faker.date_object()
        delta = timedelta(days=randint(0, 28))
        finish_date = start_date + delta
        report.started = start_date
        report.finished = finish_date
        report.workHours = (delta.days + 1) * 8
        report.description = self.faker.paragraphs(nb=6)
        report.save()
        print(report)
