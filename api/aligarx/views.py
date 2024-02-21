from serializers import TeacherProfilGetSerializers
from rest_framework.views import APIView
from rest_framework import generics
from apps.accounts.models import User
from apps.structure.permission import IsTeacher
from .serializers import TeacherProfilGetSerializers


class TeacherApiViewList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = TeacherProfilGetSerializers
    # permission_classes = IsTeacher


class TeacherApiViewUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = TeacherProfilGetSerializers
    # permission_classes = IsTeacher

