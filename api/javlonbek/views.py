from .serializers import AttendanceSerializer, GradeSerializers
from apps.structure.models import Attendance, Task_submitions
from rest_framework.generics import ListAPIView , RetrieveAPIView
from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
from apps.structure.permission import IsStudent, IsAdmin
from rest_framework.views import APIView
from rest_framework.response import Response



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
        serilizer_data = self.serializer_class(queryset, many=True)
        return Response(serilizer_data.data)

