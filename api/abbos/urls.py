from django.urls import path
from .views import TaskCreateApiView, TaskListApiView, AttendanceCreateApiView


urlpatterns = [
    path("task/", TaskListApiView.as_view()),
    path("task-create/", TaskCreateApiView.as_view()),
    path("davomat-create/", AttendanceCreateApiView.as_view()),
]
