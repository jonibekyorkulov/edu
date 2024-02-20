from django.urls import path
from .views import UploadTestApiview ,QuestionsApiView

urlpatterns = [
    path('upload-test/', UploadTestApiview.as_view()),
    path('questions/', QuestionsApiView.as_view()),

    
]