from django.shortcuts import render
from apps.structure.models import Group
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from apps.structure.permission import IsTeacher
from .serializers import ClassScheduleSerializer
from rest_framework.response import Response
class ClassScheduleView (APIView):
    permission_classes = (IsTeacher,)
    serializer = ClassScheduleSerializer
    model = Group
    def get(self, request):
        teacher_id = request.user.id
        filter_group = self.model.objects.filter(teacher_id=teacher_id)
        data_serializer = ClassScheduleSerializer(filter_group, many=True)
        if data_serializer.is_valid():
            data = {
                "status" : True,
                "data" : data_serializer.data
            }
            return Response(data)
        else:
            data = {
                "status" : False,
                "message" : "Xato"
            }