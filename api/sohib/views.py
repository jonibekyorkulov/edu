from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GroupGetRoomSerializer
from apps.structure.models import Group
from apps.accounts.models import User
from django.shortcuts import get_object_or_404


class GetTable(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        uuid = request.data.get('uuid')
        type = request.data.get('type')
        if type == 'group':
            group = get_object_or_404(Group, uuid = uuid)
            serializer = GroupGetRoomSerializer(instance=group)
            data = {
                'status' : True,
                'data' : serializer.data
            }
            return Response(data)
        elif type == 'teacher':
            teacher = get_object_or_404(User, uuid=uuid)
            groups = teacher.group_teacher
            print(groups)
            serializer = GroupGetRoomSerializer(instance=groups, many=True)
            data = {
                'status' : True,
                'data' : serializer.data
            }
            return Response(data)
        elif type == 'student':
            student = get_object_or_404(User, uuid = uuid)
            groups = student.group_student
            serializer = GroupGetRoomSerializer(instance=groups, many=True)
            data = {
                'status' : True,
                'data' : serializer.data
            }
            return Response(data)
        return Response({"status":False})
