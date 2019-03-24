from django.core.management.base import BaseCommand
from ServiceJobs.fake_data import FakeCaretaker


class Command(BaseCommand):
    help = 'Create 5 fake caretakers each related to a random hospital.'

    def handle(self, *args, **options):
        for _ in range(5):
            caretaker = FakeCaretaker()
            caretaker.populate()
