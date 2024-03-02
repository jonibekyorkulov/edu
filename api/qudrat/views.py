
from apps.accounts.models import User, UserFile
from apps.base.models import RegionModel
from apps.structure.models import Subject
from .serializers import UserCreateSerializer, UserCreateFileSerializer, SubjectSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from apps.structure.permission import IsAdmin
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import pandas as pd
from rest_framework.exceptions import ValidationError


class UserCreateApiView(CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserCreateSerializer

    queryset = User.objects.all()
    

class UserUpdateApiView(UpdateAPIView):
    permission_classes = [IsAdmin, ]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    http_method_names = ['put', 'patch']
    
    
class UserRetrieveApiView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    

class UserDeleteApiView(APIView):
    permission_classes = [AllowAny, ]
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


class WriteUserApiView(APIView):
    serializer_class = UserCreateFileSerializer
    permission_classes = [IsAdmin, ]
    
    def post(self, request):
        file = request.data['file']
        user_file = UserFile.objects.create(
            file = file
        )
        user_file.save()
        df = pd.read_excel(file)
        error_list = []
        for index, row in df.iterrows():
            passport = row['passport']
            jshir = row['jshir']
            
            passport_start = passport[:1]
            if not passport_start.isalpha():
                data = {
                    'status' : False,
                    'message' : "Your passport isn't starting with alphabetics",
                    "error_id" : 'f{row["T/r"]}'
                }
                error_list.append(data)
                continue
            if len(passport)!=9:
                data = {
                    'status' : False,
                    'message' : "Your passport isn't starting with alphabetics",
                    "error_id" : 'f{row["T/r"]}'
                }
                error_list.append(data)
                continue
            
            if type(jshir)!=int:
                data = {
                    'status' : False,
                    'message' : "Your passport isn't starting with alphabetics",
                    "error_id" : 'f{row["T/r"]}'
                }
                error_list.append(data)
                continue
              
            if len(str(jshir)) != 14:
                data = {
                    'status' : False,
                    'message' : "Your passport isn't starting with alphabetics",
                    "error_id" : 'f{row["T/r"]}'
                } 
                error_list.append(data)
                continue
            
            if User.objects.filter(username=passport).exists():
                data = {
                    'status' : False,
                    'message' : "Your passport isn't starting with alphabetics",
                    "error_id" : 'f{row["T/r"]}'
                }
                error_list.append(data)
                continue
            
            region = row['region']
            region = get_object_or_404(RegionModel, name = region)
            district = row['district']
            district = get_object_or_404(RegionModel, name = district)
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
                address = row['address'],
                password = passport,
                region = region,
                district = district
            )
            user.save()
        data = {
            'status' : True,
            'message' : "Your users created succesfully but some users have error",
            'errors' : error_list
        }
        return Response(data)
   
   
class SubjectCreateApiView(CreateAPIView):
    permission_classes = [IsAdmin, ]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()   
   

class SubjectUpdateApiView(UpdateAPIView):
    permission_classes = [IsAdmin, ]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    http_method_names = ['put', 'patch']   
   

class SubjectRetrieveApiView(RetrieveAPIView):
    permission_classes = [IsAdmin, ]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all() 
    

class SubjectDeleteApiView(APIView):
    permission_classes = [IsAdmin, ]
    serializer_class = SubjectSerializer
    
    def delete(self, request):
        user = request.data.get('uuid')
        subject = get_object_or_404(Subject, uuid=user)
        subject.is_active = False
        subject.save()
        data = {
            'status' : True,
            'data': "success"
        }
        return Response(data)   
   


