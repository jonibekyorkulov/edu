from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class UserLoginTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.username = 'admin'
        self.password = '123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_user_login_success(self):
        # Test user login with correct credentials
        url = reverse('login')  # Assuming you have a login endpoint with name 'login' in your URLs
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_user_login_failure(self):
        # Test user login with incorrect credentials
        url = reverse('login')
        data = {'username': self.username, 'password': 'wrongpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)