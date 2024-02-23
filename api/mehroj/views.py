from django.shortcuts import render
from rest_framework.generics import (ListAPIView, 
                                     CreateAPIView, 
                                     RetrieveAPIView, 
                                     UpdateAPIView, 
                                     DestroyAPIView, 
                                     ListCreateAPIView, 
                                     RetrieveUpdateDestroyAPIView,
                                     )
from rest_framework.permissions import AllowAny, IsAuthenticated
from apps.accounts.models import User,UserRol
from apps.structure.models import Room,Group,Tasks
from .serializers import GroupSerializer,RoomSerializer,BaholarSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError


class CreateRoomView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = RoomSerializer
    queryset = Room.objects.all()



class CreateGroupView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class ListBaholarView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = BaholarSerializer
    

    def get_queryset(self):  
        tasks = Tasks.objects.get(uuid = self.request.data.get('uuid') )
        return tasks.task_submitions_task_id.all()

    
    