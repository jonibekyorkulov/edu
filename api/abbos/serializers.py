from rest_framework import serializers, exceptions
from apps.structure.models import Tasks, Attendance, Group
from rest_framework.exceptions import ValidationError
from django.db.models import Q

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"

    
    def validate(self, data):
        name = data.get("name")
        deadline = data.get("deadline")
        group_id = data.get("group_id")
        
        if Tasks.objects.filter(name=name, deadline=deadline, group_id=group_id):
            data = {
                "status": False,
                "message": "Bu taskni siz yaratgansiz"
            }
            raise ValidationError(data)
        return data

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
    
    def validate(self, data):
        
        return data