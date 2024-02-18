from .serializers import AttendanceSerializers
from rest_framework import generics


class AttendanceView(generics.ListAPIView):
    serializer_class = AttendanceSerializers