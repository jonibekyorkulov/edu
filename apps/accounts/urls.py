from django.urls import path, include
from .views import LoginView, LogoutView, AccessRefreshView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view()),
    path('refresh_token/', AccessRefreshView.as_view()),

]
