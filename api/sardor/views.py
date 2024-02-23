from rest_framework.views import APIView
from apps.structure.models import Test, TestQuestion, TestAnswer, TestResult
from .serializers import UploadTestSerializer, TestQuestionSerializer
# from rest_framework.permissions import AllowAny, IsAuthenticated
from apps.structure.permission import IsAdmin, IsStudent, IsTeacher
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView
# from rest_framework.permissions import IsAuthenticated
from openpyxl import workbook, load_workbook
from django.shortcuts import get_object_or_404



class UploadTestApiview(APIView):
    serializer_class = UploadTestSerializer
    permission_classes = (IsTeacher, ) 
  
    def post(self, request):
        data = request.data
        data['tester'] = request.user.uuid
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                "status" : True,
                "message" : serializer.data,
            }
            return Response(data)


class StudentGetQuestionsApiView(APIView):
    permission_classes = (IsTeacher, )
    serializer_class = TestQuestionSerializer
    # queryset = Test.objects.all()
    

    def get(self, request, uuid):
        object = get_object_or_404(Test, uuid = uuid) 
        # file = object.
        # print(object.file.path)
        path = f"{object.file.path}"
        # print("aaaaaa",path)
        wb_obj = load_workbook(path)
        sheet_obj = wb_obj.active
        # print(sheet_obj['B2'].value)
        questions = {}
        for i in range(2, sheet_obj.max_row + 1):
            B = f'B{i}'
            C = f'C{i}'
            D = f'D{i}'
            E = f'E{i}'
            F = f'F{i}'
            question_data = {
               f"{i-1}. {sheet_obj[B].value}" : {
                                                f"A. {sheet_obj[C].value}",                                  
                                                f"B. {sheet_obj[D].value}",                                  
                                                f"C. {sheet_obj[E].value}",                                   
                                                f"D. {sheet_obj[D].value}"                                   
               } 
            }
            questions.update(question_data)
            # print(data)
 
        serializer = self.serializer_class(instance=object)
        data = {
            "status" : True,
            "data" : serializer.data,
            "questioins" : questions

        }
        return Response(data)
    

        
        
    



class QuestionsApiView(APIView):
    def get(self, request):
        pass
        
