from rest_framework import serializers
from apps.structure.models import Group
# class ClassScheduleSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 255)
#     subject_id = serializers.CharField(max_length = 255)
#     room_id = serializers.CharField(max_length = 255)
#     week_id = serializers.StringRelatedField(many=True)
#     lesson_start = serializers.TimeField()
#     lesson_end = serializers.TimeField()
    
class ClassScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'subject_id', 'room_id', 'week_id', 'lesson_start', 'lesson_end')
