from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.structure.models import Tasks
from .serializers import TaskSerializer
from rest_framework import status


class TaskCreateApiView(APIView):
    permission_classes = [
        AllowAny,
    ]
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data_task = {
                "status": True,
                "message": f"{request.user.username} task yaratdingiz",
            }
            return Response(data=data_task, status=status.HTTP_201_CREATED)
