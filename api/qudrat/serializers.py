from rest_framework import serializers
from apps.accounts.models import User, UserFile
from apps.structure.models import Subject
from rest_framework.exceptions import ValidationError


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'uuid',
            'username',
            'first_name',
            'last_name',
            'middle_name',
            'role',
            'phone_namber',
            'passport',
            'jshir',
            'gender',
            'address',
            'region',
            'district',
            'birthday',
            'photo'
        )
        

    
    def validate_passport(self, value):
        if value:
            if User.objects.filter(passport=value).exists():
                data = {
                    'status' : False,
                    'message' : "Your passport isn't unique"
                }
                raise ValidationError(data)
            passport_start = value[:1]
            passport_last = value[2:]
            if not passport_start.isalpha():
                data = {
                    'status' : False,
                    'message' : "Your passport isn't starting with alphabetics"
                }
                raise ValidationError(data)
            if len(value)!=9 or not passport_last.isdigit():
                data = {
                    'status' : False,
                    'message' : "Your passport is wrong"
                }
                raise ValidationError(data)
            
            return value
        
    def validate_jshir(self, value):
        if value:              
            if len(str(value)) != 14:
                data = {
                    'status' : False,
                    'message' : "Your JSHSHIR is wrong"
                }
            if User.objects.filter(jshir=value).exists():
                data = {
                    'status' : False,
                    'message' : "Your jshir isn't unique"
                }
                raise ValidationError(data)
            return value
        else:
            data = {
                'status' : False,
                'message' : "Your JSHSHIR isn't exists"
            }
            raise ValidationError(data)

    
class UserCreateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = ('file', 'uuid')

    
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
    
 
   
    