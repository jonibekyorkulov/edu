from rest_framework import serializers
from apps.accounts.models import User,UserRol
from apps.structure.models import Room,Week,Group
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
        return attrs
        

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        teacher = attrs['teacher_id']
        time_s = attrs['lesson_start']
        time_e = attrs['lesson_end']
        weeks = attrs['week_id']
       

        a = Group.objects.filter(teacher_id = teacher)
        for group in a:
            for week in weeks:
                if week in group.week_id.all():
                    if time_e >= time_s:
                        data = {
                                'status' : False,
                                'message' : 'These times are equal'
                            }
                        raise ValidationError(data)

                    if time_s >= group.lesson_start and time_s<=group.lesson_end:
                        data = {
                                'status' : False,
                                'message' : 'These times are equal'
                            }
                        raise ValidationError(data)
                    if time_e >= group.lesson_start and time_e <= group.lesson_end:
                        data = {
                                'status' : False,
                                'message' : 'These times are equal'
                            }
                        raise ValidationError(data)
                    if time_s < group.lesson_start and time_e > group.lesson_end:
                        data = {
                                'status' : False,
                                'message' : 'These times are equal'
                            }
                        raise ValidationError(data)
        data = attrs
        data['is_active'] = True
        return data 

                


        


        

            



        


   



        


        