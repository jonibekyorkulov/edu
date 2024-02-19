from rest_framework import serializers
from apps.accounts.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id',
            'rol',
            'first_name',
            'last_name',
            'middle_name',
            'phone_namber',
            'passport',
            'jshir',
            'gender',
            'adress',
            'region',
            'district',
            'photo',
            'birthday',
            'tg_username'
        )
        
    # def create(self, validated_data):
    #     user = super(UserCreateSerializer, self).create(validated_data)
    #     user.save()
    #     return user
    
    