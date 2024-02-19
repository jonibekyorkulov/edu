from django.urls import path
from .views import TaskCreateApiView


urlpatterns = [
    path("task-create/", TaskCreateApiView.as_view())
]
