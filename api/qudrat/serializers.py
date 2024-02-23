from rest_framework import serializers
from apps.accounts.models import User, UserFile
from apps.structure.models import Subject
from rest_framework.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'uuid',
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
            passport_start = value[:1]
            if not passport_start.isalpha():
                data = {
                    'status' : False,
                    'message' : "Your passport isn't starting with alphabetics"
                }
                raise ValidationError(data)
            if len(value)!=9:
                data = {
                    'status' : False,
                    'message' : "Your passport is wrong"
                }
                raise ValidationError(data)
            return value
        
    def validate_jshir(self, value):
        if value:
            if type(value)!=int:
                data = {
                    'status' : False,
                    'message' : "Your JSHSHIR isn't in number"
                }
                raise ValidationError(data)  
            if len(str(value)) != 14:
                data = {
                    'status' : False,
                    'message' : "Your JSHSHIR is wrong"
                }

        
    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.save()
        return user
    
    
class UserCreateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = ('file', 'uuid')

    
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
    
    
    
   
    