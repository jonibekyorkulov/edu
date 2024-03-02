from apps.structure.models import Attendance, Tasks
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from apps.accounts.models import User
from apps.structure.models import Group, Subject, Room, Lesson
from django.urls import reverse



class AttendanceTest(TestCase):
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
            self.lesson = Lesson.objects.create(
                name = 'testlesson',
                group_id = self.group,
            )
            self.attendance = Attendance.objects.create(
                student_id = self.user_data,
                lesson_id = self.lesson
            )

            

    def test_attendance(self):
        
        url = reverse('attendance-student')
        self.client.force_authenticate(user=self.user_data)
        response = self.client.get(url)  
        self.assertEqual(response.status_code, status.HTTP_200_OK) 


class GradeTest(TestCase):
     
    def setUp(self):
            self.client = APIClient()
            self.user_data = User.objects.create_user(
                username = 'aaatest',
                role = 'student'
            )
            self.teacher = User.objects.create(
                  username = 'ustoz',
                  role = 'teacher'
            )
            self.room = Room.objects.create(name='test_room')
            self.subject = Subject.objects.create(name='test_subject', duration = 1)
            self.group = Group.objects.create(
                room_id = self.room,
                subject_id = self.subject
                )
            self.task = Tasks.objects.create(
                  name = 'test_task', 
                  grade = "5",
                  deadline = '2024-03-08',
                  teacher_id = self.teacher,
                  group_id = self.group
                )
                      
    def test_grade(self):
        url = reverse("grade_student")
        self.client.force_authenticate(user = self.user_data)
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
          
          
    
           




    # def test_lesson_source(self):
    #     url = reverse('lesson_source')
    #     self.client.force_authenticate(user = self.user)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)