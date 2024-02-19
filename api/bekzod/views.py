from .serializers import AttendanceSerializers
from rest_framework import generics
from apps.structure.models import Attendance
from apps.base.enum import UserRol


class AttendanceUpdateView(generics.RetrieveAPIView):
    obj = Attendance.objects.filter(student__user__role=UserRol.STUDENT).order_by("id")
    serializer_class = AttendanceSerializers

    def get_queryset(self):
        qs = self.obj.filter(student__user__id=self.request.id)
        if qs:
            return qs
        return []
        