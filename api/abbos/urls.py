from django.urls import path
from .views import TaskCreateApiView, TaskListApiView


urlpatterns = [
    path("task/", TaskListApiView.as_view()),
    path("task-create/", TaskCreateApiView.as_view())
]
