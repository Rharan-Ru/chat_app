from django.shortcuts import render
from django.views import View
from .models import ChatRoom, Chat, Profile
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, View):
    def get(self, request):
        chats = ChatRoom.objects.all()
        return render(request, 'chat/index.html', {'chats': chats})


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
        return render(request, 'chat/room.html', {
            'room_name': room_name,
            'chats': chats,
            'room': room
        })
