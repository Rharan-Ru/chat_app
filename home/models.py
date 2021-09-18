from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Simple Post Model
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    thumb = models.ImageField(upload_to='img_post/', blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
