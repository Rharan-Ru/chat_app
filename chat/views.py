from django.shortcuts import render
from django.views import View
from .models import ChatRoom, Chat, Categorias
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.db.models import Q


# List all chats
class Index(LoginRequiredMixin, View):
    def get(self, request):
        chats = ChatRoom.objects.all()
        meus_chats = ChatRoom.objects.filter(users=request.user.pk)
        categorias = Categorias.objects.all()
        print(meus_chats)
        return render(request, 'chat/index.html', {'chats': chats, 'meus_chats': meus_chats, 'categorias': categorias})


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
        ja_esta = False
        for user in room.users.values('id'):
            if self.request.user.pk == user['id']:
                ja_esta = True

        # if ja_esta:
        #     print('ja esta - view ')
        #     pass
        # else:
        #     print('nao estava - view')
        #     room.users.add(request.user)
        #     room.save()

        context = {
            'room_name': room_name,
            'chats': chats,
            'room': room
        }

        return render(request, 'chat/room.html', context)
