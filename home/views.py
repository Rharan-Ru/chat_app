from django.shortcuts import render
from django.views import View
from home.models import Post, Comment
from chat.models import ChatRoom
from django.db.models import Count
from django.http import HttpResponseRedirect, JsonResponse


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
        if request.user.is_authenticated:
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


class RedirectURL(View):
    def get(self, request):
        print(HttpResponseRedirect(request.META.get('HTTP_REFERER')))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AddLikes(View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        likes = post.likes.all().count()
        data = {}

        if request.user in post.likes.all():
            post.likes.remove(request.user)
            data['color'] = 'text-info'

        elif request.user not in post.likes.all():
            post.likes.add(request.user)
            data['color'] = 'text-danger'

        data['likes'] = post.likes.all().count()

        post.save()
        return JsonResponse(data)
