from apps.accounts.models import User
from .serializers import UserCreateSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from apps.structure.permission import IsAdmin
from rest_framework.views import APIView

class UserCreateApiView(CreateAPIView):
    permission_classes = [IsAdmin, ]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    

class UserUpdateApiView(UpdateAPIView):
    permission_classes = [IsAdmin, ]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    http_method_names = ['put', 'patch']
    