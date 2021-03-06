from django.urls import re_path

from chat.consumers import ChatConsumer, RoomConsumer
from private_chat.consumers import PrivateChatConsumer
from home.consumers import CommentsConsumer

websocket_urlpatterns = [
    # Chat Rooms url patterns
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
    re_path(r'ws/chat/', RoomConsumer.as_asgi()),

    # Private chat url pattern
    re_path(r'ws/private_chat/thread/(?P<room_pk>\w+)/$', PrivateChatConsumer.as_asgi()),

    # Comments url patterns
    re_path(r'ws/comments/(?P<post_pk>\w+)/$', CommentsConsumer.as_asgi()),
]
