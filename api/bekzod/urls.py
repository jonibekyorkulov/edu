from django.urls import path
from api.bekzod.views import AttendanceUpdateView

urlpatterns = [
    path('nb/', AttendanceUpdateView.as_view()),
]