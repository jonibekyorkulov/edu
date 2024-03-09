from apps.structure.models import  Attendance,  Lesson, Tasks, Task_submitions
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from apps.accounts.models import User
from apps.structure.models import Group, Week, Subject, Room
from django.urls import reverse
from datetime import timedelta


# class AttendanceTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user_data = User.objects.create_user(
#             username = 'aaatest',
#             role = 'student'
#         )
#         self.room = Room.objects.create(name='test_room')
#         self.subject = Subject.objects.create(name='test_subject', duration = 1)
#         self.group = Group.objects.create(
#             room_id = self.room,
#             subject_id = self.subject
#         )
#         self.lesson = Lesson.objects.create(
#             name = 'testlesson',
#             group_id = self.group,
#         )
#         self.attendance = Attendance.objects.create(
#             student_id = self.user_data,
#             lesson_id = self.lesson
#         )

    
        

#     def test_attendance(self):
        
#         url = reverse('attendance-student')
#         self.client.force_authenticate(user=self.user_data)
#         response = self.client.get(url)  
#         print(response.data)
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK) 
        


class TestGrade(TestCase):
     
    def setUp(self) -> None:
     
        self.client = APIClient()
        self.user_data = User.objects.create_user(
            username = 'test',
            role = 'student'
        )
        self.user_data = User.objects.create(
            passport = 'AB1234567',
            role = 'student'
        )
        self.user_teach = User.objects.create(
            username = 'Jonibek',
            role = 'teacher'
        )
        self.subject = Subject.objects.create(
            name = 'Python_Django',
            duration = 1
        )
        self.room = Room.objects.create(name='test_room')
        self.group = Group.objects.create(
            room_id = self.room,
            subject_id = Subject.objects.all().first(),
            teacher_id = self.user_teach
            )
        self.group.student_id.set((User.objects.all().first(), ))

        self.lesson = Lesson.objects.create(
            name = 'testlesson',
            group_id = self.group,
        )
        
        self.task = Tasks.objects.create(
            name = 'testgrade',
            
            deadline = '2024-03-24',
            teacher_id = self.user_teach ,
            group_id = self.group,
          

        )  
        
        self.task_submition = Task_submitions.objects.create(
           
            grade = 5,
            student_id = self.user_data ,
            group_id = self.group,
        )    
        
    def test_grade(self):

        url = reverse("grade-student")
        self.client.force_authenticate(user = self.user_data)
        response = self.client.get(url)
        print(response.data,'kkkkkkkkkk')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_lesson_source(self):
    #     url = reverse('lesson-source')
    #     self.client.force_authenticate(user = self.user)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)