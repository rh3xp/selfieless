from django.db import models
from django.conf import settings

#from django.contrib.auth.models import User


class User(models.Model):
    uname = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=20)
    profile_pic = models.CharField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uname


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        ordering = ('name'),
        verbose_name = 'category',
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    uname = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    #uname = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255, verbose_name="Title")
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

