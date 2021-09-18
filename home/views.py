from django.shortcuts import render
from django.views import View
from .models import Post
from chat.models import ChatRoom
from django.db.models import Count


class Home(View):
    def get(self, request):
        posts = Post.objects.all().order_by('created_on')
        salas = ChatRoom.objects.all().annotate(num_users=Count('users')).order_by('-num_users')

        for sala in salas:
            print(sala.name)
        context = {
            'posts': posts,
            'salas': salas,
        }
        return render(request, 'home/home.html', context)
