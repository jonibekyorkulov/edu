from django.urls import path
from .views import TaskCreateApiView, TaskListApiView, AttendanceCreateApiView, AttendanceUpdateApiView, GradeJudgeApiView


urlpatterns = [
    path("task/", TaskListApiView.as_view()),
    path("task-create/", TaskCreateApiView.as_view()),
    path("davomat-create/", AttendanceCreateApiView.as_view()),
    path("davomat-update/", AttendanceUpdateApiView.as_view()),
    path("grade-create/", GradeJudgeApiView.as_view()),
]
