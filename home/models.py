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
    views = models.ManyToManyField(User, related_name='views')
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
    reply_author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='reply_author')

    def children(self):
        return Comment.objects.filter(parent=self)

    def is_parent(self):
        if self.parent is None:
            return True
        return False
