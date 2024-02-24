from apps.structure.models import Attendance
from rest_framework import serializers


class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('uuid', 'student_id', 'lesson_id', 'status')
