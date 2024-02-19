from rest_framework import serializers
from apps.accounts.models import User
from rest_framework.exceptions import ValidationError


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = '__all__'
    
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
            if value.isdigit():
                data = {
                    'status' : False,
                    'message' : "Your JSHSHIR isn't in number"
                }
                raise ValidationError(data)  
            if len(value) != 14:
                data = {
                    'status' : False,
                    'message' : "Your JSHSHIR is wrong"
                } 
        
    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.save()
        return user
    
    
   
    