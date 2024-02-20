from django.urls import path
from .views import AttendanceView


urlpatterns = [
    path('att/<uuid:uuid>/', AttendanceView.as_view() , name='attendance')
]