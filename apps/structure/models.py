from datetime import timedelta
from django.db import models
from apps.base.models import BaseModel
from apps.accounts.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.


class Room(BaseModel):

    name = models.CharField(max_length = 255, null=True, blank=True)
    size = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Week(BaseModel):

    name = models.CharField(max_length = 255, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name


class Subject(BaseModel):

    name = models.CharField(max_length = 255, null=True, blank=True)
    
    duration = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name



class Group(BaseModel):

    name = models.CharField(max_length = 255, null=True, blank=True)
    subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE, related_name = 'group_subject')
    student_id = models.ForeignKey(User, on_delete = models.SET_NULL, related_name = 'group_student',null=True)
    teacher_id = models.ForeignKey(User, on_delete = models.SET_NULL, related_name = 'group_teacher',null=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name = 'group_room')
    start_time = models.DateField(null=True, blank=True)
    end_time = models.DateField(null=True, blank=True)
    week_id = models.ForeignKey(Week, on_delete = models.SET_NULL, related_name = 'group_week', null=True)
    lesson_start = models.TimeField(null=True, blank=True)
    lesson_end = models.TimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args,**kwargs):
        self.end_time = self.start_time + timedelta(months = self.subject_id.duration)
        super(Group, self).save(*args,**kwargs)

class Lesson(BaseModel):

    name = models.CharField(max_length = 255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    group_id = models.ForeignKey(Group, on_delete = models.CASCADE, related_name = 'lesson_group')
    video = models.FileField(upload_to='lesson_video/',null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'mpeg', 'avi', 'flw', 'mov', 'mkv'])
    ])


    def __str__(self) -> str:
        return self.name


class LessonSource(BaseModel):

    file = models.FileField(upload_to='lesson_source/', null=True, blank=True)
    lesson_id = models.ForeignKey(Lesson, on_delete = models.CASCADE, related_name = 'lesson_source_lesson_id')

    def __str__(self) -> str:
        return self.lesson_id.name


class Attendance(BaseModel):

    student_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'attendance_student_id')
    lesson_id = models.ForeignKey(Lesson, on_delete = models.CASCADE, related_name = 'attendance_lesson_id')
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.student_id.full_name


class Tasks(BaseModel):
    name = models.CharField(max_length = 255, null=True, blank=True)
    grade = models.IntegerField(default=0)
    deadline = models.DateTimeField()
    group_id = models.ForeignKey(Group, on_delete = models.CASCADE, related_name = 'tasks_group_id')
    file = models.FileField(upload_to='tasks/')
    

    def __str__(self) -> str:
        return self.name


class Task_submitions(BaseModel):

    task_id = models.ForeignKey(Tasks, on_delete = models.CASCADE, related_name = 'task_submitions_task_id')
    student_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'task_submitions_student_id')
    file = models.FileField(upload_to='task_submitions/')
    grade = models.IntegerField(default=0)
    

    def __str__(self) -> str:
        return self.task_id.name
    

class Payment(BaseModel):

    student_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'payment_student_id')
    summa = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.student_id.full_name
    


    


