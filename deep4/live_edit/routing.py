from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chatroom/", consumers.ChatConsumer.as_asgi(), name="ChatConsumer"),
    re_path(
        r"ws/chatroom/(?P<room_name>\w+)/$",
        consumers.ChatConsumer.as_asgi(),
        name="ChatConsumer",
    ),
]
