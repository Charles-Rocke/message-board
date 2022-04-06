from django.db import models

# Create your models here.

# model for posts
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]