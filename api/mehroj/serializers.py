from rest_framework import serializers
from apps.accounts.models import User,UserRol


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','student_id','subject_id','teacher_id','start_time','end_time')