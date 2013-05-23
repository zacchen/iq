from django.db import models
from users.models import User
# Create your models here.

class Post(models.Model):
    title =             models.CharField()
    content =           models.TextField() 
    picture =           models.ImageField()
    created =           models.TimeField(auto_now_add=True)
    modified =          models.TimeField(auto_now=True)
    userid =            models.ForeignKey(User)

    class Meta():
        ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

class Comment(models.Model)
    content =           models.TextField() 
    created =           models.TimeField(auto_now_add=True)
    modified =          models.TimeField(auto_now=True)
    userid =            models.ForeignKey(User)
    postid =            models.ForeignKey(BPosts)

    class Meta():
        ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'
