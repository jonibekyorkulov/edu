from rest_framework.views import APIView
from apps.structure.models import Test, TestQuestion, TestAnswer, TestResult
from .serializers import UploadTestSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView


class UploadTestApiview(CreateAPIView):
    serializer_class = UploadTestSerializer
    permission_classes = (IsAuthenticated, )
    
    
    # def perform_create(self, serializer):
    #     serializer.save(user = self.request.user)
    def post(self, request, data):
        print(request)
        serializer = self.serializer_class(data = request.data, many=True)

        if serializer.is_valid(raise_exception=True):
            # Test.objects.create(user = request.user)
            print('1111111111111111111111111111111111')
            serializer.save(user = request.user)
            data = {
                "status" : True,
                "message" : "Test created",
            }
            return Response(data)

        
        
    



class QuestionsApiView(APIView):
    def get(self, request):
        pass
        
