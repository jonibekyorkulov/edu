from django.test import TestCase


# Create your tests here.

class AccountTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_login(self):
        print("Hello")
        response = self.client.login(username="admin", passeord="123")
        self.assertEqual(response.context['user'].is_active)
