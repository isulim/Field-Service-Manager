from django.core.management.base import BaseCommand
from ServiceJobs.fake_data import FakeDevice


class Command(BaseCommand):
    help = 'Create 10 fake devices each related to random hospital and a caretaker in it.'

    def handle(self, *args, **options):
        for _ in range(10):
            device = FakeDevice()
            device.populate()
