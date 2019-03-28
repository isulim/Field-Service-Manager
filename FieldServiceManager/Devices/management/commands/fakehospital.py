from django.core.management.base import BaseCommand
from Devices.devices_faker import FakeHospital


class Command(BaseCommand):
    help = 'Create 10 fake hospitals.'

    def handle(self, *args, **options):
        for _ in range(10):
            hospital = FakeHospital()
            hospital.populate()
