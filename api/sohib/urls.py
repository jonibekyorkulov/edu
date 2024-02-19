from django.urls import path, include
from .views import GroupGetRoomView

urlpatterns = [
    path("group_get_room/", GroupGetRoomView.as_view())
]