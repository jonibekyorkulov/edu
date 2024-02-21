from rest_framework import serializers
from apps.accounts.models import User
from rest_framework.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False)
    username = serializers.CharField(required=False)    
    class Meta:
        model = User
        fields = (
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
    

class UserUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(write_only = True, required = False)
    last_name = serializers.CharField(write_only = True, required = False)
    middle_name = serializers.CharField(write_only = True, required = False)
    role = serializers.CharField(write_only = True, required = False)
    phone_namber = serializers.CharField(write_only = True, required = False)
    passport = serializers.CharField(write_only = True, required = False)
    jshir = serializers.CharField(write_only = True, required = False)
    gender = serializers.CharField(write_only = True, required = False)
    address = serializers.CharField(write_only = True, required = False)
    region = serializers.CharField(write_only = True, required = False)
    district = serializers.CharField(write_only = True, required = False)
    birthday = serializers.DateField(write_only = True, required = False)
    photo = serializers.ImageField(required = False, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'heic', 'heif'])
    ])
    
    def update(self, instance, validated_data):
        super().update(instance, validated_data)
    
    
    
   
    