from rest_framework.views import APIView
from apps.structure.models import Test, TestQuestion, TestAnswer, TestResult
from .serializers import UploadTestSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class UploadTestApiview(APIView):
    serializer_class = UploadTestSerializer
    permission_classes = (AllowAny, )
    def post(self, requst):
        serializer = self.serializer_class(data = requst.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save(user = requst.user)
                data = {
                    "status" : True,
                    "message" : "Comment created",
                    "your_upload_test" : serializer.data
                }
                return Response(data)
        except Exception as e:
            data = {
                    "status" : True,
                    "message" : f"{e}",
                }
            raise ValidationError(data)

        
        
    



class QuestionsApiView(APIView):
    def get(self, request):
        pass
        
