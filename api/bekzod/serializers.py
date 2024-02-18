from ...apps.accounts.models import User
from rest_framework import serializers


class AttendanceSerializers(serializers.ModelSerializer):
    status = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = ('id', 'teacher_id', 'lesson_id', 'status')
