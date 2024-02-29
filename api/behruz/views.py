from .serializers import StudentTaskSubmittionsSerializer, StudentScheduleSerializer, ContentDownloadSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.structure.permission import IsStudent,IsTeacher,IsAdmin
from rest_framework.response import Response

class StudentTaskSubmittionView(APIView):
    permission_classes = [IsStudent]
    serializer_class = StudentTaskSubmittionsSerializer
    
    def post(self, request):
        data = request.data
        data['student_id'] = request.user.id
        serializer = StudentTaskSubmittionsSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            data = {
                'status' : 'True',
                'data' : request.data
            }
            return Response(data=data)
        else:
            return Response(serializer.errors)


class StudentScheduleView(APIView):
    
    permission_classes = [IsStudent]
    serializer_class = StudentScheduleSerializer
    
    def get(self, request):
        student = request.user
        groups = student.group_student
        serializer = StudentScheduleSerializer(instance=groups, many=True)
        data = {
            'status' : True,
            'data' : serializer.data
        }
        return Response(data)


class DownloadContentView(APIView):
    permission_classes = [IsStudent]
    serializer_class = ContentDownloadSerializer
    
    def get(self, request):
        id = request.data.get(id)
        serializer = ContentDownloadSerializer(id, many=True)
        
        data = {
            'status' : True,
            'data' : serializer.data
        }
        return Response(data)  

                


