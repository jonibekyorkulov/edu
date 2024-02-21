from .serializers import AttendanceSerializer, GradeSerializers, LessonSourceSerializer
from apps.structure.models import Attendance, Task_submitions, LessonSource
from rest_framework.response import Response
from apps.structure.permission import IsStudent, IsAdmin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated



class AttendanceView(APIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsStudent]

    def get(self, request, uuid):
    
        queryset = Attendance.objects.filter(student_id = uuid)
        serilizer_data = self.serializer_class(queryset, many=True)
        return Response(serilizer_data.data)


class GradeAPIView(APIView):
    serializer_class = GradeSerializers
    permission_classes = [IsStudent]

    def get(self, request, uuid):
        queryset =Task_submitions.objects.filter(student_id = uuid)
        serilizer_data = self.serializer_class(queryset, many = True)
        return Response(serilizer_data.data)


class LessonSourceView(APIView):
    serializer_class = LessonSourceSerializer
    permission_classes = [IsStudent]

    def get(self,request,  uuid):
        queryset = LessonSource.objects.filter(lesson_id = uuid)
        serializer_data = self.serializer_class(queryset, many = True)
        return Response(serializer_data.data)
