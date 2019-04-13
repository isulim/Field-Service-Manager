from django.contrib.auth.models import User
from django.test import TestCase
from random import randint, sample
from faker import Faker
from Devices.models import Hospital, Device, DeviceType, Caretaker


class HospitalTestCase(TestCase):

    def create_hospital(self, code, diff):
        hospitals_before = Hospital.objects.count()
        new_hospital = {
            'name': '{}'.format(self.faker.company()),
            'city': '{}'.format(self.faker.city()),
            'address': '{}'.format(self.faker.street_address()),
            'phone': '{}'.format(self.faker.phone_number()),
            'email': '{}'.format(self.faker.email())
        }
        response = self.client.post('/hospital/create/', new_hospital)
        self.assertEqual(response.status_code, code)
        self.assertEqual(Hospital.objects.count(), (hospitals_before + diff))

    def setUp(self):
        self.faker = Faker('pl_PL')

    def test_get_hospital_list(self):
        response = self.client.get('/hospital/')
        self.assertEqual(response.status_code, 200)

    def test_get_hospital(self):
        response = self.client.get('/hospital/{}/'.format(randint(1, Hospital.objects.count())))
        self.assertEqual(response.status_code, 200)

    def test_post_hospital_with_permission(self):
        self.client.login(username='biuro', password='biuro')
        self.create_hospital(302, 1)

    def test_post_hospital(self):
        self.create_hospital(200, 0)

    def test_update_hospital(self):
        self.client.login(username='biuro', password='biuro')
        new_hospital = {
            'name': '{}'.format(self.faker.company()),
            'city': '{}'.format(self.faker.city()),
            'address': '{}'.format(self.faker.street_address()),
            'phone': '{}'.format(self.faker.phone_number()),
            'email': '{}'.format(self.faker.email())
        }
        response = self.client.post('/hospital/update/1', new_hospital)
        self.assertEqual(response.status_code, 302)
