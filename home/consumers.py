import json

from django.contrib.auth.models import User

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from home.models import Comment, Post
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
            post = await database_sync_to_async(Post.objects.get)(pk=self.post_pk)
            comment_post = Comment(
                author=self.scope['user'],
                post=post,
                comment=comment,
            )
            await database_sync_to_async(comment_post.save)()
            num_comments = await database_sync_to_async(comment_post.replies.count)()
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'comment': comment,
                    'author': self.scope['user'].username,
                    'user_profile': user_profile.image.url,
                    'com_pk': comment_post.pk,
                    'num_comments': num_comments,
                }
            )
        else:
            reply = text_data_json['reply']
            parent_id = text_data_json['parent_id']
            reply_author = text_data_json['reply_author']
            span_comment = text_data_json['span_comment']

            rep_author = await database_sync_to_async(User.objects.get)(username=reply_author)
            await database_sync_to_async(print)(rep_author.username)

            parent_comment = await database_sync_to_async(Comment.objects.get)(pk=parent_id)
            post = await database_sync_to_async(Post.objects.get)(pk=self.post_pk)
            comment_reply = Comment(
                author=self.scope['user'],
                post=post,
                comment=reply,
                parent=parent_comment,
                reply_author=rep_author
            )
            await database_sync_to_async(comment_reply.save)()
            num_comments = await database_sync_to_async(parent_comment.replies.count)()
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'reply': reply,
                    'author': self.scope['user'].username,
                    'user_profile': user_profile.image.url,
                    'reply_pk': comment_reply.pk,
                    'reply_author': rep_author.username,
                    'parent_pk': parent_comment.pk,
                    'span_comment': span_comment,
                    'num_comments': num_comments,
                }
            )

    async def chat_message(self, event):
        if 'comment' in event:
            comment = event['comment']
            user_profile = event['user_profile']
            author = event['author']
            com_pk = event['com_pk']
            num_comments = event['num_comments']
            await self.send(text_data=json.dumps({
                'comment': comment,
                'user_profile': user_profile,
                'author': author,
                'com_pk': com_pk,
                'num_comments': num_comments,
            }))
        else:
            reply = event['reply']
            user_profile = event['user_profile']
            author = event['author']
            reply_pk = event['reply_pk']
            reply_author = event['reply_author']
            parent_pk = event['parent_pk']
            span_comment = event['span_comment']
            num_comments = event['num_comments']
            await self.send(text_data=json.dumps({
                'reply': reply,
                'user_profile': user_profile,
                'author': author,
                'reply_pk': reply_pk,
                'reply_author': reply_author,
                'parent_pk': parent_pk,
                'span_comment': span_comment,
                'num_comments': num_comments,
            }))
