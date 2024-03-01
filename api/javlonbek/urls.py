from django.urls import path
from .views import AttendanceView, GradeAPIView, LessonSourceView


urlpatterns = [
    path('attendance/<uuid:uuid>/', AttendanceView.as_view() , name='attendance_student'), 
    path('grade/<uuid:uuid>/', GradeAPIView.as_view() , name='grade_student'), 
    path('lessonsource/<uuid:uuid>/', LessonSourceView.as_view(), name = "lesson_source"),


]