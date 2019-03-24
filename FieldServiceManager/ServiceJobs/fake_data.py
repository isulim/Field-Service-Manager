from datetime import timedelta, datetime

from faker import Faker
from random import randint
from ServiceJobs.models import Hospital, Device, Job, Report, Caretaker


class FakeHospital:
    faker = Faker('pl_PL')

    def populate(self, n=1):
        """Create fake n hospitals in database.
            n default = 1"""
        for _ in range(n):
            hospital = Hospital()
            hospital.name = self.faker.company()
            hospital.city = self.faker.city()
            hospital.address = self.faker.address()
            hospital.phone = self.faker.phone_number()
            hospital.email = self.faker.email()
            hospital.save()
            print(hospital)


class FakeCaretaker:
    faker = Faker('pl_PL')

    def populate(self):
        """Create fake caretaker person related to hospital."""

        hospital_count = Hospital.objects.all().count()

        caretaker = Caretaker()
        caretaker.firstName = self.faker.first_name()
        caretaker.lastName = self.faker.last_name()
        caretaker.phone = self.faker.phone_number()
        caretaker.email = self.faker.email()
        caretaker.hospital = Hospital.objects.get(pk=randint(1, hospital_count))
        caretaker.save()
        print(caretaker)


class FakeDevice:
    faker = Faker('en_US')

    def populate(self):
        """Create fake device in database related to random hospital and an caretaker."""

        caretaker_count = Caretaker.objects.all().count()

        device = Device()
        device.sn = self.faker.ean(13)
        device.deviceType = randint(1, 12)
        device.manufacturer = randint(1, 9)
        device.modelName = self.faker.word()
        installation = self.faker.date_object()
        device.installation = installation
        device.guaranteeDate = installation + timedelta(days=730)
        maintenance = self.faker.date_between_dates(date_start=(installation + timedelta(days=183)),
                                                    date_end=datetime.now())
        device.lastMaintenance = maintenance
        device.nextMaintenance = maintenance + timedelta(days=180)
        caretaker = Caretaker.objects.get(pk=randint(1, caretaker_count))
        device.caretaker = caretaker
        device.hospital = caretaker.hospital
        device.save()
        print(device)

