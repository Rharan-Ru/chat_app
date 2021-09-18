from django.shortcuts import render
from django.views import View
from .models import ChatRoom, Chat
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.db.models import Q


# List all chats
class Index(LoginRequiredMixin, View):
    def get(self, request):
        chats = ChatRoom.objects.all()
        return render(request, 'chat/index.html', {'chats': chats})


# Create a chatroom if is not created and get all chat messages inside it
class Room(LoginRequiredMixin, View):
    def get(self, request, room_name):
        room = ChatRoom.objects.filter(name=room_name).first()
        chats = []

        if room:
            chats = Chat.objects.filter(room=room)
        else:
            room = ChatRoom(name=room_name)
            room.save()

        room.users.add(request.user)
        room.save()

        context = {
            'room_name': room_name,
            'chats': chats,
            'room': room
        }

        return render(request, 'chat/room.html', context)
