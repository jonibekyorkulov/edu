from django.urls import path, include
from views import StudentTaskSubmittionView, StudentScheduleView

urlpatterns = [
    path("task-submit/<int:pk>/",StudentTaskSubmittionView.as_view(), name="task-submit"),
    path("schedule-student/", StudentScheduleView.as_view(), name="schedule-student")
    
]