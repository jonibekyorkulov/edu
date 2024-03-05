
from django.urls import path

from .views import (
    UserCreateApiView,
    UserUpdateApiView, 
    UserRetrieveApiView,
    UserDeleteApiView,
    WriteUserApiView,
    SubjectCreateApiView,
    SubjectUpdateApiView,
    SubjectRetrieveApiView,
    SubjectDeleteApiView
)


urlpatterns = [
    path('create-user/', UserCreateApiView.as_view(), name="create_user"),
    path('update-user/<uuid:pk>/', UserUpdateApiView.as_view(), name='update_user'),
    path('retrieve-user/<uuid:pk>/', UserRetrieveApiView.as_view(), name="retrieve_user"),
    path('delete/', UserDeleteApiView.as_view(), name = 'delete_user'),
    path('user-file/', WriteUserApiView.as_view()),
    path('subject-create/', SubjectCreateApiView.as_view(), name= 'create_subject'),
    path('subject-update/<uuid:pk>/', SubjectUpdateApiView.as_view(), name= 'update_subject'),
    path('subject-retrieve/<uuid:pk>/', SubjectRetrieveApiView.as_view(), name= 'retrieve_subject'),
path('subject-delete/', SubjectDeleteApiView.as_view(), name= 'delete_subject'),
]
