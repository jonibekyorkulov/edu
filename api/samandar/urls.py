from rest_framework.urls import path
from .views import ClassScheduleView
urlpatterns = [
    path('class-schedule/', ClassScheduleView.as_view())
]