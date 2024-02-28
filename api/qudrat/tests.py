from django.test import TestCase
from apps.accounts.models import User
from django.urls import reverse
from django.contrib.auth import get_user

class UserCreateTestCase(TestCase):
    