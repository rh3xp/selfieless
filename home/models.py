from django.db import models

# Create your models here.

class profile(models.Model):
    uname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=20)
    profile_pic = models.CharField(max_length=1000)
