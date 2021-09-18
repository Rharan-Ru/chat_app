from django.urls import re_path

from .consumers import PrivateChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/private/(?P<room_name>\w+)/$', PrivateChatConsumer.as_asgi()),
]
