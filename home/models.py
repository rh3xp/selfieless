from django.db import models

# Create your models here.

class Users(models.Model):
    uname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=20)
    profile_pic = models.CharField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uname + '-' + str(self.created)

class posts(models.Model):
    posts_uname = models.ForeignKey(Users, on_delete=models.CASCADE)
    categories = models.CharField(max_length=100)
