from django.urls import path
from api.bekzod.views import AttendanceRetrieveApiView

urlpatterns = [
    path('attendance-retrieve', AttendanceRetrieveApiView.as_view(), name='attendance-retrieve'),
    
]