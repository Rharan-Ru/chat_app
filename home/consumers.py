import json

from django.contrib.auth.models import User

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from private_chat.models import ThreadModel, MessageModel
from chat.models import Profile


class CommentsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.post_pk = self.scope['url_route']['kwargs']['post_pk']
        self.room_group_name = 'post_%s' % self.post_pk

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        user_profile = await database_sync_to_async(Profile.objects.get)(user=self.scope['user'])
        text_data_json = json.loads(text_data)

        if 'comment' in text_data_json:
            comment = text_data_json['comment']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'comment': comment,
                    'username': self.scope['user'].username,
                    'user_profile': user_profile.image.url,
                }
            )
        else:
            reply = text_data_json['reply']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'reply': reply,
                    'username': self.scope['user'].username,
                    'user_profile': user_profile.image.url,
                }
            )

    async def chat_message(self, event):
        if 'comment' in event:
            comment = event['comment']
            user_profile = event['user_profile']
            username = event['username']
            await self.send(text_data=json.dumps({
                'comment': comment,
                'user_profile': user_profile,
                'username': username,
            }))
        else:
            reply = event['reply']
            user_profile = event['user_profile']
            username = event['username']
            await self.send(text_data=json.dumps({
                'reply': reply,
                'user_profile': user_profile,
                'username': username,
            }))
