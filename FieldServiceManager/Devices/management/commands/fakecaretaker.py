from django.core.management.base import BaseCommand
from Devices.devices_faker import FakeCaretaker


class Command(BaseCommand):
    help = 'Create 15 fake caretakers each related to a random hospital.'

    def handle(self, *args, **options):
        for _ in range(15):
            caretaker = FakeCaretaker()
            caretaker.populate()
