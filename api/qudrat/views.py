from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from apps.accounts.models import User
from .serializers import UserCreateSerializer
from rest_framework.generics import CreateAPIView

class UserCreateApiView(CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()