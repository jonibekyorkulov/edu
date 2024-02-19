from .serializers import AttendanceSerializers
from rest_framework import generics
from apps.structure.models import Attendance
from apps.base.enum import UserRol


class AttendanceView(generics.ListAPIView):
    serializer_class = AttendanceSerializers