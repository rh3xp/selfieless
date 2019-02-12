from django.db import models

# Create your models here.

class profile(models.Model):
    uname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=20)
    profile_pic = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uname + '-' + self.email

class posts(models.Model):
    posts_uname = models.ForeignKey(profile, on_delete=models.CASCADE)
    categories = models.CharField(max_length=100)
