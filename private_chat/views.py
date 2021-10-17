from django.views import View
from .models import ThreadModel, MessageModel
from chat.models import ChatRoom
from chat.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.db.models import Q


class ListThreads(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
        salas_user = ChatRoom.objects.filter(users=request.user)

        context = {
            'threads': threads,
            'salas_user': salas_user
        }
        return render(request, 'private_chat/inbox.html', context)


class CreateThread(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        receiver = profile.user

        if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
            thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
            return redirect('thread', pk=thread.pk)
        elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
            thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
            return redirect('thread', pk=thread.pk)

        thread = ThreadModel(
            user=request.user,
            receiver=receiver
        )
        thread.save()

        return redirect('thread', pk=thread.pk)


class ThreadView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        messages = MessageModel.objects.filter(thread__pk__contains=pk)
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
        mess = MessageModel.objects.all().order_by('-date')
        salas_user = ChatRoom.objects.filter(users=request.user)

        context = {
            'thread': thread,
            'threads': threads,
            'messages': messages,
            'mess': mess,
            'salas_user': salas_user,
        }
        return render(request, 'private_chat/thread.html', context)

    def test_func(self):
        pk = self.kwargs.get('pk')
        thread = ThreadModel.objects.get(pk=pk)
        if self.request.user == thread.user or self.request.user == thread.receiver:
            return True
