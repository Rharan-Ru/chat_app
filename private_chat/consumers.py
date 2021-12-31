import json

from django.contrib.auth.models import User

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from private_chat.models import ThreadModel, MessageModel
from chat.models import Profile


class PrivateChatConsumer(AsyncWebsocketConsumer):
    """
    This consumer has all private messages logic

    def connect - Just connect the user to the channel layer room, and save room_pk information.

    def disconnect - This only discard the users from channel layer, in other words he is disconnected.

    def receive - This method receive messages from web-socket and send to the room group, if user send a message
    the receive update the database with this new message.
    Also save the users messages and send back to the channel layer room group.

    def chat_message - Send back all channel layer room group messages to the frontend with all nescessary
    message informations.
    """
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_pk']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        self.room_name = self.scope['url_route']['kwargs']['room_pk']

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.user_id = self.scope['user'].id
        self.user_name = self.scope['user'].username

        user_profile = await database_sync_to_async(Profile.objects.get)(user=self.scope['user'])
        user_receiver = await database_sync_to_async(User.objects.get)(id=text_data_json['receiver_name'])

        thread = await database_sync_to_async(ThreadModel.objects.get)(pk=self.room_name)
        messages = MessageModel(thread=thread, sender_user=self.scope['user'],
                                receiver_user=user_receiver, text=message)

        await database_sync_to_async(messages.save)()

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
