from django.urls import path
from .views import AttendanceView


urlpatterns = [
    path('attendance/<int:student_id>/<int:lesson_id>/', AttendanceView.as_view(), name='Attendance')
]