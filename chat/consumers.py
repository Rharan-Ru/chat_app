import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatRoom, Chat, Profile
from django.core.serializers import serialize


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user_name = self.scope['user'].username

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()
        room = await database_sync_to_async(ChatRoom.objects.get)(name=self.room_name)
        await database_sync_to_async(room.users.add)(self.scope['user'])
        await database_sync_to_async(room.save)()

        num_users = await database_sync_to_async(room.users.all)()
        num_users = await database_sync_to_async(len)(num_users)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': '',
                'user_id': '',
                'user_name': '',
                'entrou': f'{self.scope["user"].username} entrou na sala',
                'num_users': num_users
            }
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        room = await database_sync_to_async(ChatRoom.objects.get)(name=self.room_name)
        await database_sync_to_async(room.users.remove)(self.scope['user'])
        await database_sync_to_async(room.save)()

        num_users = await database_sync_to_async(room.users.all)()
        num_users = await database_sync_to_async(len)(num_users)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': '',
                'user_id': '',
                'user_name': '',
                'entrou': f'{self.scope["user"].username} saiu da sala',
                'num_users': num_users
            }
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.user_id = self.scope['user'].id
        self.user_name = self.scope['user'].username

        user_profile = await database_sync_to_async(Profile.objects.get)(user=self.scope['user'])

        room = await database_sync_to_async(ChatRoom.objects.get)(name=self.room_name)
        chat = Chat(
            content=message,
            user=self.scope['user'],
            room=room,
        )
        await database_sync_to_async(chat.save)()

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': self.user_id,
                'user_name': self.user_name,
                'user_profile': user_profile.image.url,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        if event['message']:
            message = event['message']
            user_id = event['user_id']
            user_name = event['user_name']
            user_profile = event['user_profile']
            await self.send(text_data=json.dumps({
                'message': message,
                'user_id': user_id,
                'user_name': user_name,
                'user_profile': user_profile
            }))
        else:
            entrou = event['entrou']
            num_users = event['num_users']
            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'entrou': entrou,
                'num_users': num_users
            }))
