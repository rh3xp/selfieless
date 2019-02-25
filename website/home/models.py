from django.db import models
from django.conf import settings

from django.contrib.auth.models import User


class User(models.Model):
    uname = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=20)
    profile_pic = models.CharField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uname + '-' + str(self.created)


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        ordering = ('name'),
        verbose_name = 'category',
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255, verbose_name="Title")
    text = models.TextField()

    def __str__(self):
        return self.title

