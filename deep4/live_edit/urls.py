# chat/urls.py
from django.urls import path

from . import views

app_name = "live_edit"

urlpatterns = [
    path("chatroom/", views.index, name="index"),
    path("chatroom/<str:room_name>/", views.room, name="room"),
]
