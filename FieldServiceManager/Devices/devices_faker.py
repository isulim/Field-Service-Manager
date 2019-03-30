from datetime import timedelta, datetime

from faker import Faker
from random import randint, choice
from Devices.models import Hospital, Device, Caretaker, DeviceType, Manufacturer


class FakeHospital:
    faker = Faker('pl_PL')

    def populate(self):
        """Create fake hospital in database"""
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

    models = {
        1: ['Reflect', 'Evening', 'Edge'],
        2: ['Senior', 'Manage', 'System'],
        3: ['Major', 'Hit', 'Head'],
        4: ['Hope', 'Place', 'Expert'],
        5: ['Artist', 'Total', 'Best'],
        6: ['Hand', 'Follow', 'Focus'],
        7: ['Change', 'Move', 'Key'],
        8: ['Style', 'Life', 'Coach'],
    }

    def populate(self):
        """Create fake device in database related to random hospital and an caretaker."""

        caretaker_count = Caretaker.objects.all().count()
        device_type_count = DeviceType.objects.all().count()
        manufacturer_count = Manufacturer.objects.all().count()
        device = Device()
        device.sn = self.faker.ean(13)
        device.deviceType = DeviceType.objects.get(pk=(randint(1, device_type_count)))
        manufacturer = Manufacturer.objects.get(pk=(randint(1, manufacturer_count)))
        device.manufacturer = manufacturer
        device.modelName = choice(self.models[manufacturer.id])
        installation = self.faker.date_this_decade(before_today=True, after_today=False)
        device.installation = installation
        device.guaranteeDate = installation + timedelta(days=730)
        maintenance = self.faker.date_between_dates(date_start=(installation + timedelta(days=183)),
                                                    date_end=(installation + timedelta(days=3650)))
        device.lastMaintenance = maintenance
        device.nextMaintenance = maintenance + timedelta(days=180)
        caretaker = Caretaker.objects.get(pk=randint(1, caretaker_count))
        device.caretaker = caretaker
        device.hospital = caretaker.hospital
        device.save()
        print(device)

