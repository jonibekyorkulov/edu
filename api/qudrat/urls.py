
from django.urls import path
from .views import (
    UserCreateApiView,
    UserUpdateApiView, 
    UserRetrieveApiView,
    UserDeleteApiView,
    UserCreateFileApiView,
    WriteUserApiView
)

urlpatterns = [
    path('create-user/', UserCreateApiView.as_view()),
    path('update-user/<uuid:pk>/', UserUpdateApiView.as_view()),
    path('retrieve-user/<uuid:pk>/', UserRetrieveApiView.as_view()),
    path('delete/', UserDeleteApiView.as_view()),
    path('user-create-file/', UserCreateFileApiView.as_view()),
    path('user-file/<uuid:uuid>/', WriteUserApiView.as_view()),
]
