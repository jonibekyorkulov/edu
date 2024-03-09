from rest_framework import routers
from django.urls import path
from .views import TeacherApiViewList
# TeacherApiViewUpdate

urlpatterns = [
    path('teacherlist/<uuid:uuid>/', TeacherApiViewList.as_view())
]