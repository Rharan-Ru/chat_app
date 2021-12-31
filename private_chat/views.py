from django.views import View
from .models import ThreadModel, MessageModel, SolicitaModel
from chat.models import ChatRoom
from chat.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.db.models import Q


class Solicita(View):
    """
    This classView create a solicitation contact to destinatary user
    """
    def get(self, request, pk, *args, **kwargs):
        destinatario = Profile.objects.get(pk=pk)
        if not SolicitaModel.objects.filter(remetente=request.user, destinatario=destinatario.user).exists():
            solicitacao = SolicitaModel(
                remetente=request.user,
                destinatario=destinatario.user
            )
            solicitacao.save()

        return redirect('profile', pk=pk)


class ListThreads(LoginRequiredMixin, View):
    """
    List all contacts users
    """
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
        salas_user = ChatRoom.objects.filter(users=request.user)
        mess = MessageModel.objects.all().order_by('-date')

        context = {
            'threads': threads,
            'salas_user': salas_user,
            'mess': mess,

        }
        return render(request, 'private_chat/inbox.html', context)


class RemoveSolicita(View):
    """
    Decline solicitation contact
    """
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        receiver = profile.user

        solicitacao = SolicitaModel.objects.filter(remetente=receiver, destinatario=request.user)
        solicitacao.delete()

        return redirect('inbox')


class CreateThread(LoginRequiredMixin, View):
    """
    Create a new thread, a new user contact if you don't have contact before
    """
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        receiver = profile.user

        solicitacao = SolicitaModel.objects.filter(remetente=receiver, destinatario=request.user)
        solicitacao.delete()

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
        print(thread)
        thread.save()

        return redirect('thread', pk=thread.pk)


class ThreadView(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    Get thread users information to list all mensages, users rooms and users last mensages from another chat
    """
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
        # Test mixin to garant acess for only users in the private room
        pk = self.kwargs.get('pk')
        thread = ThreadModel.objects.get(pk=pk)
        if self.request.user == thread.user or self.request.user == thread.receiver:
            return True
