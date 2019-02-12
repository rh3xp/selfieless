from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h1>this is the index fx in home</h1>")

def profile(request, user_id):
    return HttpResponse("<h2>User id: " + str(user_id) + "</h2>")
