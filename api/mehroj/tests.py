from apps.accounts.models import User
from apps.structure.models import Subject,Room,Week
from rest_framework import status 
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse




class CreateGroupTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'admin',
            'password': '123',
            'role': 'admin',
        }
        self.user = User.objects.create_user(**self.user_data)
        self.token = Token.objects.create(user = self.user)
        self.client.login(username="admin", password="123", role = "admin")


        self.teacher =User.objects.create(
            passport = 'AB1234567',
            jshir = 12345678901234,
            role = 'teacher'
        )
        self.teacher.save()


        self.student = User.objects.create(
            passport = 'AB1234568',
            jshir = 12345678901235,
            role = 'student'
        )
        self.student.save()

        self.subject = Subject.objects.create(
            duration = 6
        )
        self.subject.save()

        self.room = Room.objects.create(
            size = 30
        )
        self.room.save()

        self.week = Week.objects.create(
            name = 'dushanba'

        )
        self.week.save()




    
    def test_group_post(self):
        url = reverse('create-group')
        self.client.force_authenticate(user = self.user)
        

        data = {
            'name' : 'ABCDEFG',
            'subject_id':f"{Subject.objects.all().first().uuid}",
            'student_id':[f"{User.objects.filter(role='student').first().uuid}"],
            'teacher_id':f"{User.objects.filter(role='teacher').first().uuid}",
            'room_id':f"{Room.objects.all().first().uuid}",
            'week_id':[f"{Week.objects.all().first().uuid}"],
            'lesson_start':'11:00:00',
            'lesson_end':'17:00:00'

            
        }
        
        response = self.client.post(url, data=data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


