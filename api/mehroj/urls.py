from django.urls import path
from .views import CreateGroupView,RetrieveAPIView,UpdateAPIView,DeleteGroupView


urlpatterns = [
    path('create_group/', CreateGroupView.as_view()),
    path('update_group/', UpdateAPIView.as_view()),
    path('retrieve_view/', RetrieveAPIView.as_view()),
    path('delete_group/', DeleteGroupView.as_view()),



]