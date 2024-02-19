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
from apps.structure.models import Room
from .serializers import GroupSerializer,RoomSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError




# class  CreateGroupView(CreateAPIView):
#     permission_classes = (AllowAny, )
#     queryset = User.objects.all()
#     serializer_class = GroupSerializer

# class UpdateGroupView(UpdateAPIView):
#     permission_classes = (AllowAny, )
#     queryset = User.objects.all()
#     serializer_class = GroupSerializer

#     def get_queryset(self):
#         queryset = User.objects.filter(user = self.request.user, id = self.kwargs['pk'])
#         return queryset
    
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         if not  instance :
#             return Response("Cannot update USER", status=status.HTTP_400_BAD_REQUEST)
#         self.perform_update(instance)
        
#         data ={
#             'message':'User is updated'
            
#         }
#         return Response(data)

# class RetrieveGroupView(RetrieveAPIView):
#     permission_classes = (AllowAny, )
#     queryset = User.objects.all()
#     serializer_class = GroupSerializer

# class DeleteGroupView(DestroyAPIView):
#     serializer_class = GroupSerializer
#     permission_classes = [IsAuthenticated, ]

#     # def get_queryset(self):
#     #     queryset = User.objects.filter(user = self.request.user, id=self.kwargs['pk'])
#     #     return queryset

#     # def destroy(self, request, *args, **kwargs):
#     #     instance = self.get_object()
#     #     if not  instance :
#     #         return Response("Cannot delete USER", status=status.HTTP_400_BAD_REQUEST)
#     #     self.perform_destroy(instance)
        
#     #     data ={
#     #         'message':'User is deleted'
            
#     #     }
#     #     return Response(data)
class CreateRoomView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    
    