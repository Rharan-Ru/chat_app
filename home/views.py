from django.shortcuts import render
from django.views import View
from home.models import Post, Comment
from chat.models import ChatRoom
from django.db.models import Count


class Home(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('created_on')
        salas = ChatRoom.objects.all().annotate(num_users=Count('users')).order_by('-num_users')

        context = {
            'posts': posts,
            'salas': salas,
        }
        return render(request, 'home/home.html', context)


class PostDetail(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        salas = ChatRoom.objects.all().annotate(num_users=Count('users')).order_by('-num_users')
        post.views.add(request.user)
        context = {
            'post': post,
            'salas': salas,
        }
        return render(request, 'home/post_detail.html', context)


class HomeTag(View):
    def get(self, request, tag, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        if tag == 'destaques':
            posts = Post.objects.all().order_by('-views')
        salas = ChatRoom.objects.all().annotate(num_users=Count('users')).order_by('-num_users')

        context = {
            'posts': posts,
            'salas': salas,
        }
        return render(request, 'home/home.html', context)
