from django.urls import path
from .views import UploadTestApiview , StudentGetQuestionsApiView

urlpatterns = [
    path('upload-test/', UploadTestApiview.as_view()),
    path('test-questions/<uuid:uuid>/', StudentGetQuestionsApiView.as_view()),

    
]