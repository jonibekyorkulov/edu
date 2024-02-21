from apps.accounts.models import User
from .serializers import UserCreateSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from apps.structure.permission import IsAdmin
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

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