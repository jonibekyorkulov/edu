from .serializers import AttendanceSerializers
from rest_framework import generics


class AttendanceUpdateView(generics.RetrieveAPIView):
    serializer_class = AttendanceSerializers

    