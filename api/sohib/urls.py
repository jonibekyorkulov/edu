from django.urls import path, include
from .views import GetTable

urlpatterns = [
    path("get_table/", GetTable.as_view())
]