from django.shortcuts import render
from django.views import View
from home.models import Post, Comment
from chat.models import ChatRoom
from django.db.models import Count
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('created_on')

        context = {
            'posts': posts,
        }
        return render(request, 'home/home.html', context)


class PostDetail(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        if request.user.is_authenticated:
            post.views.add(request.user)
        context = {
            'post': post,
        }
        return render(request, 'home/post_detail.html', context)


class HomeTag(View):
    def get(self, request, tag, *args, **kwargs):
        if tag == 'destaques':
            posts = Post.objects.all().order_by('-views')
            context = {'posts': posts}
            return render(request, 'home/home.html', context)
        elif tag == 'mais_votados':
            num_posts = Post.objects.all().count()
            posts = Post.objects.all().order_by('-likes')[0:num_posts]
            context = {'posts': posts}
            return render(request, 'home/home.html', context)
        elif tag == 'novos':
            posts = Post.objects.all().order_by('-created_on')
            context = {'posts': posts}
            return render(request, 'home/home.html', context)
        return render(request, 'home/home.html')


class RedirectURL(View):
    def get(self, request):
        print(HttpResponseRedirect(request.META.get('HTTP_REFERER')))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AddLikes(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        likes = post.likes.all().count()
        data = {}

        if request.user in post.likes.all():
            post.likes.remove(request.user)
            data['color'] = 'text-dark'

        elif request.user not in post.likes.all():
            post.likes.add(request.user)
            data['color'] = 'text-danger'
            if request.user in post.deslikes.all():
                post.deslikes.remove(request.user)
                data['color_c'] = 'text-dark'

        data['likes'] = post.likes.all().count()

        post.save()
        return JsonResponse(data)


class AddDeslikes(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        likes = post.likes.all().count()
        data = {}

        if request.user in post.deslikes.all():
            post.deslikes.remove(request.user)
            data['color'] = 'text-dark'

        elif request.user not in post.deslikes.all():
            post.deslikes.add(request.user)
            data['color'] = 'text-danger'
            if request.user in post.deslikes.all():
                post.likes.remove(request.user)
                data['color_c'] = 'text-dark'

        data['likes'] = likes
        post.save()
        return JsonResponse(data)
