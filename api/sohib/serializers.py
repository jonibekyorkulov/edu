from rest_framework import serializers
from apps.structure.models import Group, Payment, Attendance


class GroupGetRoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('name', 'subject_id', 'week_id', 'lesson_start', 'lesson_end')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'