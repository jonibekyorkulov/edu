from rest_framework import routers
from django.urls import path
from views import TeacherApiViewList, TeacherApiViewUpdate



urlpatterns = [
    path('api/v1/teachelist/', TeacherApiViewList.as_view()),
    path('api/v1/teacherlist/<uuid:uuid>/', TeacherApiViewUpdate.as_view())
]