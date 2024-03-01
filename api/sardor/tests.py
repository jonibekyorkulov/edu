from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient

class UploadTestTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.upload_test_dat = {
            
        }