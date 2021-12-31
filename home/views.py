from django.shortcuts import render, redirect
from django.views import View
from home.models import Post, Comment
from chat.models import ChatRoom, Profile
from private_chat.models import ThreadModel, SolicitaModel
from django.db.models import Count
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max


class Home(View):
    """
    List all posts order by most views
    """
    def get(self, request, *args, **kwargs):
        posts = Post.objects.annotate(most_views=Max("views")).order_by('-most_views')
        context = {
            'posts': posts,
        }
        return render(request, 'home/home.html', context)


class ProfileView(View):
    """
        Users profile View that list all posts user and verify if user maked contact with you or not
    """
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        posts = Post.objects.all().filter(author=profile.user).order_by('created_on')

        contato = False
        solicitado = False
        fazer_contato = False
        thread = {}
        # Verify if user alrealy make contact with the other user
        if ThreadModel.objects.filter(user=request.user, receiver=profile.user).exists():
            contato = True
            thread = ThreadModel.objects.filter(user=request.user, receiver=profile.user)[0]
        elif ThreadModel.objects.filter(user=profile.user, receiver=request.user).exists():
            contato = True
            thread = ThreadModel.objects.filter(user=profile.user, receiver=request.user)[0]

        # Verify if alrealy send request contact for the another user or if you will accept the contact
        if SolicitaModel.objects.filter(remetente=request.user, destinatario=profile.user).exists():
            solicitado = True
        elif SolicitaModel.objects.filter(remetente=profile.user, destinatario=request.user).exists():
            fazer_contato = True

        context = {
            'profile': profile,
            'posts': posts,
            'contato': contato,
            'solicitado': solicitado,
            'fazer_contato': fazer_contato,
            'thread': thread,
        }

        return render(request, 'home/profile.html', context)


class PostDetail(View):
    """
    Get the post details
    """
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        if request.user.is_authenticated:
            post.views.add(request.user)
        context = {
            'post': post,
        }
        return render(request, 'home/post_detail.html', context)


class HomeTag(View):
    """
    Sort the posts for most view, most liked or new posts
    """
    def get(self, request, tag, *args, **kwargs):
        if tag == 'destaques':
            posts = Post.objects.annotate(most_views=Max("views")).order_by('-most_views')
            context = {'posts': posts}
            return render(request, 'home/home.html', context)
        elif tag == 'mais_votados':
            num_posts = Post.objects.all().count()
            posts = Post.objects.annotate(most_likes=Max("likes")).order_by('-most_likes')
            context = {'posts': posts}
            return render(request, 'home/home.html', context)
        elif tag == 'novos':
            posts = Post.objects.annotate(created=Max("created_on")).order_by('-created')
            context = {'posts': posts}
            return render(request, 'home/home.html', context)
        return render(request, 'home/home.html')


class RedirectURL(View):
    """
    This class redirect the user to previous page when make login
    """
    def get(self, request):
        print(HttpResponseRedirect(request.META.get('HTTP_REFERER')))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AddLikes(LoginRequiredMixin, View):
    """
    Logic for like post,  and return data in json format for Ajax function
    """
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
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
    """
    Logic for dislike post, and return data in json format for Ajax function
    """
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
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

        data['likes'] = post.likes.all().count()
        post.save()
        return JsonResponse(data)
