from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GroupGetRoomSerializer
from apps.structure.models import Group
from django.shortcuts import get_object_or_404


class GroupGetRoomView(APIView):
    serializer_class = GroupGetRoomSerializer
    model = Group
    def post(self, request):
        """
            group id
            start time
            end time
            room id
        """
        serializer = self.serializer_class(request.data)
        serializer.is_valid(raise_exception=True)
        group_id = serializer.data['group_id']
        start_time = serializer.data['start_time']
        end_time = serializer.data['end_time']
        room_id = serializer.data['room_id']
        group = get_object_or_404(self.model, uuid = group_id)
        group.start_time = start_time
        group.end_time = end_time
        group.room_id = room_id
        group.save()
        data = {
            'status' : True,
            'data': group
        }
        return Response(data)
