from django.urls import path
from .views import GetTable, GetPayment, GetAttendance, UpdateAttendance, GetStudentAttendance

urlpatterns = [
    path("get_table/", GetTable.as_view(), name="get_table"),
    path("get_payment/", GetPayment.as_view(), name='get_payment'),
    path('get_attendance_group/<uuid:uuid>/', GetAttendance.as_view(), name='get_attendance_group'),
    path('update_attendance/<uuid:uuid>/', UpdateAttendance.as_view(), name='update_attendance'),
    path('get_attendance/<uuid:uuid>/', GetStudentAttendance.as_view(), name='get_attendance'),
]