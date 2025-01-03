from django.db import models


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
