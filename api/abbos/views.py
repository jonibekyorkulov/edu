from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.structure.models import Tasks, Attendance, Group, Task_submitions
from .serializers import TaskSerializer, AttendanceSerializer, GradeSerializer
from rest_framework import status, exceptions
from django.db.models import Q

from datetime import datetime
from apps.structure.permission import IsTeacher, IsStudent, IsAdmin, IsAuthenticated


class TaskCreateApiView(APIView):
    permission_classes = [
        IsTeacher,
    ]
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def post(self, request):
        try:
            request.data["teacher_id"] = request.user.uuid
        except:
            error_data = {"status": False, "message": "Bu user mavjud emas"}
            raise exceptions.ValidationError(error_data)
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data_task = {
                "status": True,
                "message": f"{request.user.username} task yaratdingiz",
            }
            return Response(data=data_task, status=status.HTTP_201_CREATED)


class TaskListApiView(APIView):
    permission_classes = (IsTeacher, IsStudent)

    def get(self, request):
        try:
            user = request.user.uuid
            tasks = Tasks.objects.filter(
                (Q(teacher_id=user) | Q(group_id__student_id=user))
                & Q(deadline__gte=datetime.now())
            )
            serializer = TaskSerializer(tasks, many=True)
            data = {"status": True, "data": serializer.data}
            return Response(data=data)
        except Exception as e:
            error = {"status": False, "message": f"{e} shunday xatolik"}
            raise exceptions.ValidationError(error)


class AttendanceCreateApiView(APIView):
    permission_classes = (IsTeacher,)
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def post(self, request):
        try:
            teacher = request.user.uuid
            lesson = request.data["lesson_id"]
            group = Group.objects.filter(Q(lesson_group=lesson) & Q(teacher_id=teacher))
            if group == False:
                error_data = {
                    "status": False,
                    "message": "Bu teacher yo dars tori kemadi",
                }
                raise exceptions.ValidationError(error_data)
        except:
            error_data = {"status": False, "message": "Bu teacher yo dars tori kemadi"}
            raise exceptions.ValidationError(error_data)

        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data_davomat = {
                "status": True,
                "message": f"{request.user.username} davomat qilindi",
            }
            return Response(data=data_davomat, status=status.HTTP_201_CREATED)


class AttendanceUpdateApiView(APIView):
    permission_classes = (IsAdmin,)

    def put(self, request):
        request.data["status"] = False
        data = request.data
        attendance = Attendance.objects.filter(
            student_id=data.get("student_id"), lesson_id=data.get("lesson_id")
        ).first()

        serializer = AttendanceSerializer(data=data, instance=attendance, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {"status": True, "message": "Sababli qilindi"}
            return Response(data)


class GradeJudgeApiView(APIView):
    permission_classes = (IsTeacher,)
    queryset = Task_submitions.objects.all()
    serializer_class = GradeSerializer

    def put(self, request):
        data = request.data
        task_sub = Task_submitions.objects.filter(
            Q(task_id=data.get("task_id"))
            & Q(student_id=data.get("student_id"))
            & Q(task_id__teacher_id=request.user.uuid)
        ).first()
        if task_sub:
            serializer = self.serializer_class(
                data=data, instance=task_sub, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data = {"status": True, "message": "Baholandi"}
                return Response(data=data)
