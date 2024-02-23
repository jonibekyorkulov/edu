from django.urls import path
from .views import UploadTestApiview, StudentResultApiView

urlpatterns = [
    path('upload-test/', UploadTestApiview.as_view()),
    path('test-questions/', StudentResultApiView.as_view()),

    
]