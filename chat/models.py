from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save


# Simple user profile
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile', on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='img_profile/', default="img_profile/default.jpg", blank=True)

    # def method to create a user profile when some new user is created
    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


# Class to save chats menssages
class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey('ChatRoom', on_delete=models.CASCADE)


# Organize chats categories
class Categorias(models.Model):
    categoria = models.CharField(max_length=255, blank=True)


# Class to create a chatroom
class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    image = models.ImageField(upload_to='img_room/', default="img_room/default.jpg", blank=True)
    categ = models.ManyToManyField(Categorias, default='Geral')
