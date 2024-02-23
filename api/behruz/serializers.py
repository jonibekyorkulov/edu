from apps.structure.models import Task_submitions, Group
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class StudentTaskSubmittionsSerializer(serializers.Serializer):
    
    file = serializers.FileField(required=True)
    task_id = serializers.CharField(max_length=255, required=True)
    
    
class StudentScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('name','subject_id','week_id','lesson_start','lesson_end')

class ContentDownloadSerializer(serializers.Serializer):
    
    lesson_source_id = serializers.CharField(max_length=255, required=True)
    