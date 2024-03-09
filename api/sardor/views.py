from rest_framework.views import APIView
from apps.structure.models import Test, TestQuestion, TestAnswer, TestResult, Group
from .serializers import UploadTestSerializer, TestQuestionSerializer, TestResultSerializer
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
        group = Group.objects.get(uuid=request.data.get('group'))
        if group.teacher_id.uuid != data['tester']:
            data = {
                
                "status": False,
                "message": "Ushbu guruhga test yuklash vakolati sizda yo'q!!!"
            }
            raise ValidationError(data)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            path = f"{serializer.instance.file.path}"
            wb_obj = load_workbook(path)
            sheet_obj = wb_obj.active
            for i in range(2, 11):
                Q = f'B{i}'
                A = f'C{i}'
                B = f'D{i}'
                C = f'E{i}'
                D = f'F{i}'

                test_question = TestQuestion.objects.create(
                    test = serializer.instance,
                    question = sheet_obj[Q].value

                )  
                test_question.save()
                TestAnswer.objects.create(question = test_question, answer = sheet_obj[A].value, status = True)                # for ans in answers_list:
                TestAnswer.objects.create(question = test_question, answer = sheet_obj[B].value, status = False)                # for ans in answers_list:
                TestAnswer.objects.create(question = test_question, answer = sheet_obj[C].value, status = False)                # for ans in answers_list:
                TestAnswer.objects.create(question = test_question, answer = sheet_obj[D].value, status = False)                # for ans in answers_list:
                         

            data = {
                "status" : True,
                # "message" : serializer.data,
            }
            return Response(data)
        
        

class StudentResultApiView(APIView):
    def post(self, request):
        test_id = request.data['test_id']
        test = get_object_or_404(Test, uuid = test_id)
        test_questions = test.test_question.all()
        data = request.data.get('data')
        ca=0
        ans = []
        for i in data:
            question = test_questions.get(uuid=i[0])
            answer = question.question_answer.get(uuid=i[1])
            if not answer in ans:
                ans.append(answer)
                if answer.status == True:
                    ca+=1
        data = {
            "student" : request.user.uuid, 
            "test" : test.uuid,
            "grade": ca
        }
        serializer = TestResultSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data":serializer.data})

