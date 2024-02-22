from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import update_last_login


class LoginSerializer(TokenObtainPairSerializer):
    def init(self, *args, **kwargs) -> None:
        super(LoginSerializer, self).init(*args, **kwargs)
        # self.fields['username'] = serializers.CharField(required=False, read_only=True)

    def auth_validate(self, data):
        password = data.get('password')
        username = data.get('username')
        

        user_kwargs = {
            self.username_field: username,
            "password": password
        }



        user = authenticate(**user_kwargs)
        if user is not None:
            self.user = user
        else:
            data = {
                'status': False,
                'message': 'User yoki parol xato'
            }
            raise ValidationError(data)



    def validate(self, data):
        self.auth_validate(data)

        data = self.user.token
        data['full_name'] = self.user.full_name

        return data
    

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class AccessRefreshSerializer(TokenRefreshSerializer):
    def validate(self, data):
        data = super().validate(data)
        access_token_instance = AccessToken(data['access'])
        user_id = access_token_instance['user_id']
        user = get_object_or_404(User, uuid = user_id)
        update_last_login(None, user)

        return data