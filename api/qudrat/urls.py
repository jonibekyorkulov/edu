
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
    path('create-user/', UserCreateApiView.as_view()),
    path('update-user/<uuid:pk>/', UserUpdateApiView.as_view()),
    path('retrieve-user/<uuid:pk>/', UserRetrieveApiView.as_view()),
    path('delete/', UserDeleteApiView.as_view()),
    path('user-file/', WriteUserApiView.as_view()),
    path('subject-create/', SubjectCreateApiView.as_view()),
    path('subject-update/<uuid:pk>/', SubjectUpdateApiView.as_view()),
    path('subject-retrieve/<uuid:pk>/', SubjectRetrieveApiView.as_view()),
    path('subject-delete/', SubjectDeleteApiView.as_view()),
]
