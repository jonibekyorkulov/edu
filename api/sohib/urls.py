from django.urls import path
from .views import GetTable, GetPayment, GetAttendance, UpdateAttendance, GetStudentAttendance

urlpatterns = [
    path("get_table/", GetTable.as_view()),
    path("get_payment/", GetPayment.as_view()),
    path('get_attendance_group/', GetAttendance.as_view()),
    path('update_attendance/<uuid:pk>', UpdateAttendance.as_view()),
    path('get_attendance/', GetStudentAttendance.as_view()),
]