from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')


class MessageModel(models.Model):
    thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)


class SolicitaModel(models.Model):
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remetente')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinatario')
