from django.urls import path
from api.bekzod.views import AttendanceListCreateApiView, AttendanceRetrieveView

urlpatterns = [
    path('nb/', AttendanceUpdateView.as_view()),
    
]