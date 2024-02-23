from rest_framework import serializers, exceptions
from apps.structure.models import Tasks, Attendance, Group, Task_submitions, Lesson
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
            data = {"status": False, "message": "Bu taskni siz yaratgansiz"}
            raise ValidationError(data)
        return data


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"

    def validate(self, data):
        group = Group.objects.filter(
            student_id=data.get("student_id"), lesson_group=data.get("lesson_id")
        ).first()
        if group is None:
            error = {"status": False, "message": "Bu student boshqa gruppadan"}
            raise exceptions.ValidationError(error)
        return data


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_submitions
        fields = ["grade", "task_id", "student_id"]
        extra_kwargs = {
            "grade": {"required": True}
        }


class LessonSerializer(serializers.ModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     super(LessonSerializer, self).__init__(*args, **kwargs)
    #     self.fields["teacher"] = serializers.CharField(max_length=250)
    class Meta:
        model = Lesson
        fields = ["name", "date", "group_id", "video"]

    # def validate(self, data):
    #     print(data.get("teacher"), "----0----0------------------------------------")
    #     return data
