from django.core.management.base import BaseCommand
from ServiceJobs.fake_data import FakeHospital


class Command(BaseCommand):
    help = 'Create 5 fake hospitals.'

    def handle(self, *args, **options):
        for _ in range(5):
            hospital = FakeHospital()
            hospital.populate()
