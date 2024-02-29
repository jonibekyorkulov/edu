from django.urls import path
from .views import CreateRoomView, CreateGroupView,ListBaholarView


urlpatterns =[
    path('create_room/', CreateRoomView.as_view(), name="create_room"),
    path('create_group/',CreateGroupView.as_view()),
    path('list_grade/',ListBaholarView.as_view()),
    

]
