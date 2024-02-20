from django.urls import path, include
from .views import GetTable, GetPayment

urlpatterns = [
    path("get_table/", GetTable.as_view()),
    path("get_payment/", GetPayment.as_view()),

]