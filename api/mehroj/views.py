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
from apps.structure.models import Room,Group
from .serializers import GroupSerializer,RoomSerializer
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

    
    