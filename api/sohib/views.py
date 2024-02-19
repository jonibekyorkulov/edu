from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GroupGetRoomSerializer
from apps.structure.models import Group
from django.shortcuts import get_object_or_404


class GetTable(APIView):
    def get(self, request):
        group = request.data.get('group_id', '')
        teacher = request.data.get('teacher_id', '')
        type = request.data.get('type')
        if type == 'group':
            group = get_object_or_404(Group, uuid = group)
