
from django.urls import path
from .views import TeacherProfileList, TeacherProfileUpdate


urlpatterns = [
    path('teacher_profile/<uuid:uuid>', TeacherProfileList.as_view()),
    path('teacher_profile_update/', TeacherProfileUpdate.as_view())
]