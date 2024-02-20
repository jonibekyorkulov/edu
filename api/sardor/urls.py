from django.urls import path
from .views import QuestionsApiView

urlpatterns = [
    path('questions/', QuestionsApiView.as_view())
    
]