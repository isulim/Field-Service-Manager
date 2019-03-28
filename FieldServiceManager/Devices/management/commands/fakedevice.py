from django.core.management.base import BaseCommand
from Devices.devices_faker import FakeDevice


class Command(BaseCommand):
    help = 'Create 30 fake devices each related to random hospital and a caretaker in it.'

    def handle(self, *args, **options):
        for _ in range(30):
            device = FakeDevice()
            device.populate()
