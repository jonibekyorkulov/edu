from django.urls import path
from .views import AttendanceView, GradeAPIView, LessonSourceView


urlpatterns = [
    path('attendance/', AttendanceView.as_view() , name = 'attendance-student'), 
    path('grade/', GradeAPIView.as_view() , name='grade_student'), 
    path('lessonsource/', LessonSourceView.as_view(), name = "lesson_source"),


]