from django.db import models
from django.contrib.auth.models import User

from posts.models import Post


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.task

    @classmethod
    def OneToManyField(cls, Paper, related_name, on_delete, primary_key):
        pass
