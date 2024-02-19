from apps.structure.models import Attendance, Task_submitions, Lesson
from rest_framework import serializers


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = Attendance
        fields = ['lesson_id', 'status']



