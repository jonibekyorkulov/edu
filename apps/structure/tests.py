from apps.structure.models import Room
from rest_framework.authtoken.models import Token
from apps.base.enum import UserRol
from apps.accounts.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class CreateRoomTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='admin',
            password='123'
        )
    
    def test_create_room_success(self):
        url = reverse("create_room")
        self.client.force_authenticate(user=self.user)
        data = {
            'name' : 'room_name',
            'size' : 25
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('name', response.data)
        self.assertIn('size', response.data)

    def test_create_room_error(self):
        url = reverse("create_room")
        self.client.force_authenticate(user=self.user)
        data = {
            'name' : 'room_name',
            'size' : "aa"
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ScheduleStudentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'admin',
            'password': '123',
            'role': 'student'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.token = Token.objects.create(user=self.user)
        self.client.login(username="admin", password="123")
        
    
    def test_schedule_get(self):
        url = reverse("schedule-student")
        self.client.force_authenticate(user=self.user)
        # print(self.user.role)
        response = self.client.get(url)
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        
        
            

        
