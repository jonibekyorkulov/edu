from apps.structure.models import Attendance
from rest_framework import serializers

class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('id', 'student_id', 'lesson_id', 'status')