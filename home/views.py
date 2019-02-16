from django.shortcuts import render
from django.http import Http404
from .models import Users


# Create your views here.

def index(request):
    all_users = Users.objects.all()
    return render(request, 'home/index.html', {'all_users' : all_users})

def detail(request, user_id):
    try:
        user = Users.objects.get(pk=user_id)
    except Users.DoesNotExist:
        raise Http404("User not found")

    return render(request, 'home/detail.html', {'user' : user})
