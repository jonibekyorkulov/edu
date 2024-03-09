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
    username = serializers.SerializerMethodField("get_username")
    user_full_name = serializers.SerializerMethodField("get_user_full_name")
    lesson = serializers.SerializerMethodField("get_lesson")
    student_id = serializers.CharField(required= False)
    lesson_id = serializers.CharField(required= False)

    class Meta:
        model = Attendance
        fields = '__all__'

    @staticmethod
    def get_username(obj):
        return obj.student_id.username
    
    @staticmethod
    def get_lesson(obj):
        return obj.lesson_id.name

    @staticmethod
    def get_user_full_name(obj):
        return obj.student_id.full_name
    
    