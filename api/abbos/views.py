from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from edu.apps.structure.models import Tasks
from .serializers import TaskSerializer


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
