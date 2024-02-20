from apps.structure.models import Attendance, Task_submitions
from rest_framework import serializers

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = '__all__'


class GradeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Task_submitions
        fields = ['task_id' , 'student_id' , 'grade']



