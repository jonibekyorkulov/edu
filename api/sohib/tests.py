from apps.structure.models import Room, Group, Subject, Payment, Lesson, Attendance
from apps.accounts.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse   

class TakePaymentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='admin',
            password='123',
            role='admin'
        )
        self.user_data = User.objects.create_user(
            username = 'aaatest',
            role = 'student',
            first_name = 'Test'
        )
        self.payment = Payment.objects.create(student_id = self.user_data)
        self.client.force_authenticate(user=self.user)
    
    def test_take_payment_success(self):
        url = reverse('get_payment')
        data = {
            'uuid': self.user_data.uuid,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_take_payment_error(self):
        url = reverse('get_payment')
        data = {
            'uuid': self.user.uuid,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertIn('status', response.data)
        self.assertEqual(response.data.get('status'), False)

class DashboardTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='admin',
            password='123',
            role='admin'
        )
        self.user_data = User.objects.create_user(
            username = 'aaatest',
            role = 'student'
        )
        self.room = Room.objects.create(name='test_room')
        self.subject = Subject.objects.create(name='test_subject', duration = 1)
        self.group = Group.objects.create(
            room_id = self.room,
            subject_id = self.subject
            )
        # self.client.force_authenticate(user=self.user)

    def test_dashboard_success(self):
        url = reverse('get_table')
        data = {
            'uuid' : self.group.uuid,
            'type' : 'group'
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data', response.data)

        data = {
            'uuid' : self.user_data.uuid,
            'type' : 'student'
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data', response.data)

    def test_dashboard_error(self):
        url = reverse('get_table')
        data = {
            'uuid' : self.group.uuid,
            'type' : 'test'
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('status', response.data)
        self.assertEqual(response.data.get('status'), False)

    def test_dashboard_error_0(self):
        url = reverse('get_table')
        data = {
            'uuid' : self.user_data.uuid,
            'type' : 'group'
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class AttendanceTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='admin',
            password='123',
            role='admin'
        )
        self.user_data = User.objects.create_user(
            username = 'aaatest',
            role = 'student'
        )
        self.room = Room.objects.create(name='test_room')
        self.subject = Subject.objects.create(name='test_subject', duration = 1)
        self.group = Group.objects.create(
            room_id = self.room,
            subject_id = self.subject
            )
        self.group.student_id.set((self.user_data, ))
        self.group.save()
        self.lesson = Lesson.objects.create(
            name = 'testlesson',
            group_id = self.group,
        )
        self.attendance = Attendance.objects.create(
            student_id = self.user_data,
            lesson_id = self.lesson
        )
    
    def test_get_group_attendance_success(self):
        data = {
            'uuid' : self.group.uuid,
        }
        url = reverse('get_attendance_group', kwargs=data)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_group_attendance_error(self):
        data = {
            'uuid' : self.room.uuid,
        }
        url = reverse('get_attendance_group', kwargs=data)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class AttendanceUpdateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.user_data = User.objects.create_user(
            username = 'aaatest',
            role = 'student'
        )
        self.room = Room.objects.create(name='test_room')
        self.subject = Subject.objects.create(name='test_subject', duration = 1)
        self.group = Group.objects.create(
            room_id = self.room,
            subject_id = self.subject
            )
        self.group.student_id.set((self.user_data, ))
        self.group.save()
        self.lesson = Lesson.objects.create(
            name = 'testlesson',
            group_id = self.group,
        )
        self.attendance = Attendance.objects.create(
            student_id = self.user_data,
            lesson_id = self.lesson
        )
    
    def test_update_attendance_success(self):
        data = {
            'uuid' : self.attendance.uuid,
        }
        changedata = {
            'status' : False
        }
        url = reverse('update_attendance', kwargs=data)
        response = self.client.put(url, data=changedata, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('student_id', response.data)
        self.assertIn('status', response.data)
        self.assertEqual(response.data['status'], False)
        self.assertEqual(response.data['lesson_id'], self.lesson.name)

    def test_update_attendance_error(self):
        data = {
            'uuid' : self.user_data.uuid,
        }
        changedata = {
            'status' : False
        }
        url = reverse('update_attendance', kwargs=data)
        response = self.client.put(url, data=changedata, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
class AttendanceStudentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = User.objects.create_user(
            username = 'aaatest',
            role = 'student'
        )
        self.room = Room.objects.create(name='test_room')
        self.subject = Subject.objects.create(name='test_subject', duration = 1)
        self.group = Group.objects.create(
            room_id = self.room,
            subject_id = self.subject
            )
        self.group.student_id.set((self.user_data, ))
        self.group.save()
        self.lesson = Lesson.objects.create(
            name = 'testlesson',
            group_id = self.group,
        )
        self.attendance = Attendance.objects.create(
            student_id = self.user_data,
            lesson_id = self.lesson
        )
    
    def test_update_attendance_success(self):
        data = {
            'uuid' : self.user_data.uuid,
        }
        url = reverse('get_attendance', kwargs=data)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('student_id', response.data[0])
        self.assertIn('status', response.data[0])

    def test_update_attendance_error(self):
        data = {
            'uuid' : self.attendance.uuid,
        }
        url = reverse('get_attendance', kwargs=data)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

