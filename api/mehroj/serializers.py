from rest_framework import serializers
from apps.accounts.models import User,UserRol
from apps.structure.models import Room
from rest_framework.response import Response
from rest_framework.validators import ValidationError


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','student_id','subject_id','teacher_id','start_time','end_time')

    def validate(self, data):
        teacher =  data.get('group_teacher', None)
        print(teacher)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        
        if Room.objects.filter(name = attrs['name']).exists():
            data = {
                'status' : False,
                'message' : 'Room already exists'
            } 
            raise ValidationError(data)


        


   



        


        