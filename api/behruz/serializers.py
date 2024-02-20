from apps.structure.models import Task_submitions
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class StudentTaskSubmittionsSerializer(serializers.Serializer):
    
    file = serializers.FileField(required=True)
    task_id = serializers.CharField(max_length=255, required=True)
    
    
