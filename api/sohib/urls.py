from django.urls import path
from .views import GetTable, GetPayment, GetAttendance

urlpatterns = [
    path("get_table/", GetTable.as_view()),
    path("get_payment/", GetPayment.as_view()),
    path('get_attendance/', GetAttendance.as_view()),
]