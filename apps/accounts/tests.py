# In your tests.py file

from apps.accounts.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse

class UserAuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'admin',
            'password': '123',
        }
        self.user = User.objects.create_user(**self.user_data)
        self.token = Token.objects.create(user=self.user)
        self.client.login(username="admin", password="123")

    def test_user_login(self):
        url = reverse("login")  # Replace with your actual login endpoint
        response = self.client.post(url, data=self.user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_invalid_user_login(self):
        url = reverse("login")  # Replace with your actual login endpoint
        invalid_user_data = {
            'username': 'nonexistentuser',
            'password': 'invalidpassword',
        }
        response = self.client.post(url, data=invalid_user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('access', response.data)
        self.assertNotIn('refresh', response.data)

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("create_user") 
        self.user_data = {
            'passport': 'AC1235874',
            'role': 'teacher',
        }
        self.user = User.objects.create_user(
            username='admin',
            password='123'
        )
    
    
    def test_user_registration(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.register_url, data=self.user_data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='AC1235874').username, 'AC1235874')

    def test_duplicate_user_registration(self):
        
        # Create a user with the same username or email before testing registration
        # User.objects.create_user(**data)

        self.client.post(self.register_url, data=self.user_data, format='json')
        response = self.client.post(self.register_url, data=self.user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 2)  # No additional user should be created
