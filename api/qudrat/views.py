from apps.accounts.models import User, UserFile
from .serializers import UserCreateSerializer, UserCreateFileSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from apps.structure.permission import IsAdmin
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import pandas as pd
from rest_framework.exceptions import ValidationError

class UserCreateApiView(CreateAPIView):
    permission_classes = [IsAdmin, ]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    

class UserUpdateApiView(UpdateAPIView):
    permission_classes = [IsAdmin, ]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    http_method_names = ['put', 'patch']
    
    
class UserRetrieveApiView(RetrieveAPIView):
    permission_classes = [IsAdmin, ]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    

class UserDeleteApiView(APIView):
    permission_classes = [IsAdmin, ]
    serializer_class = UserCreateSerializer
    
    def delete(self, request):
        user = request.data.get('uuid')
        user = get_object_or_404(User, uuid=user)
        user.is_active = False
        user.save()
        data = {
            'status' : True,
            'data': "success"
        }
        return Response(data)
    
    
class UserCreateFileApiView(CreateAPIView):
    serializer_class = UserCreateFileSerializer
    permission_classes = [IsAdmin, ]
    queryset = UserFile.objects.all()



class WriteUserApiView(APIView):
    serializer_class = UserCreateFileSerializer
    permission_classes = [IsAdmin, ]
    
    def get(self, request, uuid):
        file = UserFile.objects.filter(uuid = uuid, is_active = True).first()
        df = pd.read_excel(file.file.path)
        for index, row in df.iterrows():
            passport = row['passport']
            jshir = row['jshir']
            if User.objects.filter(username=passport).exists():
                data = {
                    'status' : False,
                    'message' : 'This username already exists'
                }
                raise ValidationError(data)
            user = User.objects.create_user(
                username = passport,
                first_name = row['first_name'],
                last_name = row['last_name'],
                middle_name = row['middle_name'],
                role = row['role'],
                phone_namber = row['phone_namber'],
                passport = passport,
                jshir = jshir,
                gender = row['gender'],
                address = row['address']
            )
            user.save()
        return Response("salom")    
    