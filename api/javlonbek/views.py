from .serializers import AttendanceSerializer, GradeSerializer
from apps.structure.models import Attendance, Task_submitions
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class AttendanceView(ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        lesson_id = self.kwargs['lesson_id']
        return Attendance.objects.filter(student_id = student_id, lesson_id = lesson_id, status = False)
    

class Gradeview(ListAPIView):
    serializer_class = GradeSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        student_id = self.kwargs['student_id']
        return Task_submitions.objects.filter(task_id = task_id, student_id = student_id)