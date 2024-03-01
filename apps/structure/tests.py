from apps.structure.models import Room
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
        
        