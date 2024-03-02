from apps.accounts.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from apps.base.models import RegionModel
from api.qudrat.serializers import UserCreateSerializer
from datetime import datetime, date
from apps.structure.models import Group, Room, Subject, Test

class UserCreateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.region = RegionModel.objects.create(
            name = "Toshkent shahar"
        )
        self.region_2 = RegionModel.objects.create(
            name = 'Yunusobod tumani',
        )
        
        self.user_update = User.objects.create(
            passport='CA7654321',
            role='student',
            first_name='Sasuke',
            middle_name='Fugaku',
            last_name='Uchiha',
            phone_namber='11-111-11-11',
            jshir=98765432109876,
            gender='erkak',
            address='Itachi',
            birthday='1997-07-23'
        )
        self.user_update.save()
        
        self.user_data = {
            'passport': 'AC1235874',
            'role': 'teacher',
            'first_name' : 'Naruto',
            'middle_name' : 'Minato',
            'last_name' : 'Uzumaki',
            'phone_namber' : '00-000-00-00',
            'jshir' : 21212121212122,
            'gender' : 'erkak',
            'address' : 'konoha',
            'region' : f'{RegionModel.objects.first().uuid}',
            'district' : f'{RegionModel.objects.last().uuid}',
            'birthday' : '1997-10-10'
        }
                
        self.user = User.objects.create_user(
            username='admin',
            password='123',
            role = 'admin'
        )
        

    def test_user_registration(self):
        self.register_url = reverse("create_user")  
        self.client.force_authenticate(user=self.user)        
        serializer = UserCreateSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertIsInstance(instance.jshir, int)
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(instance.passport, self.user_data['passport'])
        self.assertEqual(instance.role, self.user_data['role'])
        self.assertEqual(instance.first_name, self.user_data['first_name'])
        self.assertEqual(instance.middle_name, self.user_data['middle_name'])
        self.assertEqual(instance.phone_namber, self.user_data['phone_namber'])
        self.assertEqual(instance.gender, self.user_data['gender'])
        self.assertEqual(instance.address, self.user_data['address'])
        self.assertEqual(instance.jshir, self.user_data['jshir'])
        self.assertEqual(instance.region.uuid, RegionModel.objects.first().uuid)
        self.assertEqual(instance.district.uuid, RegionModel.objects.last().uuid)
        self.assertEqual(instance.birthday, date(1997, 10, 10))


    def test_duplicate_user_registration(self):
        self.register_url = reverse("create_user")  
        self.client.post(self.register_url, data=self.user_data, format='json')
        response = self.client.post(self.register_url, data=self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 3)
        
        
    def test_update_user(self):
        self.userupdate = {
            'passport' : 'DD1234567',
            'role' : 'teacher',
            'first_name' : 'Boruto',
            'middle_name' : 'Naruto',
            'last_name' : 'Uzumaki',
            'phone_namber' : '77-777-77-77',
            'jshir' : 12345123451234,
            'gender' : 'erkak',
            'address' : 'Manga',
            'birthday' : '2010-12-12'
        }
        self.update_url = f"qudrat/update-user/{User.objects.filter(role='admin').first().uuid}/"
        self.client.force_authenticate(user=self.user)        
        serializer = UserCreateSerializer(data=self.userupdate)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertIsInstance(instance.jshir, int)
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(instance.passport, self.userupdate['passport'])
        self.assertEqual(instance.role, self.userupdate['role'])
        self.assertEqual(instance.first_name, self.userupdate['first_name'])
        self.assertEqual(instance.middle_name, self.userupdate['middle_name'])
        self.assertEqual(instance.phone_namber, self.userupdate['phone_namber'])
        self.assertEqual(instance.gender, self.userupdate['gender'])
        self.assertEqual(instance.address, self.userupdate['address'])
        self.assertEqual(instance.jshir, self.userupdate['jshir'])
        self.assertEqual(instance.birthday, date(2010, 12, 12))
        
        
    def test_not_update_user(self):
        self.update_url = f'qudrat/update-user/{User.objects.last().uuid}/'
        response = self.client.patch(self.update_url, data=self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        
    def test_retrieve_user(self):
        self.client.force_authenticate(user=self.user)
        self.uuid = User.objects.get(first_name="Sasuke").uuid
        self.url = reverse('retrieve_user', kwargs={'pk': self.uuid})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['passport'], 'CA7654321')
        self.assertEqual(response.data['role'], 'student')
        self.assertEqual(response.data['first_name'], 'Sasuke')
        self.assertEqual(response.data['middle_name'], 'Fugaku')
        self.assertEqual(response.data['last_name'], 'Uchiha')
        self.assertEqual(response.data['phone_namber'], '11-111-11-11')
        self.assertEqual(response.data['gender'], 'erkak')
        self.assertEqual(response.data['jshir'], 98765432109876)
        self.assertEqual(response.data['address'], 'Itachi')
        
        
    def test_not_retrieve_user(self):
        self.url = reverse('retrieve_user', kwargs={'pk': '2a6577de-34b7-4b0d-b927-9efcf16b694a'})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        
    def test_delete_user(self):
        self.delete_data = {
            'uuid' : User.objects.all().first().uuid
        }
        self.client.force_authenticate(user=self.user)        
        self.delete_url = reverse('delete_user')
        response = self.client.delete(self.delete_url, data=self.delete_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.all().first().is_active, False)
    
    
    def test_not_retrieve_user(self):
        self.delete_data = {
            'uuid' : '2a6577de-34b7-4b0d-b927-9efcf16b694a'
        }
        self.delete_url = reverse('delete_user')
        response = self.client.delete(self.delete_url, data=self.delete_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)    
        

