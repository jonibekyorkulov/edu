from django.urls import path
from .views import CreateRoomView, CreateGroupView,ListBaholarView


# urlpatterns =[
#     path('create_group/',CreateGroupView.as_view()),
#     path('update_group/',UpdateGroupView.as_view()),
#     path('retrieve_group/',RetrieveGroupView.as_view()),
#     path('delete_group/', DeleteGroupView.as_view()),
# ]
###### XONA YARATISH 
urlpatterns =[
    path('create_room/', CreateRoomView.as_view()),
    path('create_group/',CreateGroupView.as_view()),
    path('list_grade/',ListBaholarView.as_view()),
    

]
