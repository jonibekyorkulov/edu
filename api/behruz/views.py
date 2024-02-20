from serializers import StudentTaskSubmittionsSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny, IsAuthenticated
from requests import Response

class StudentTaskSubmittionView(APIView):
    permission_classes = [IsAuthenticated]
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
