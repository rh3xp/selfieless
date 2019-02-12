from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Users


# Create your views here.

def index(request):
    all_users = Users.objects.all()
    template = loader.get_template('home/index.html')

    context = {
            'all_users' : all_users,
        }
    '''
    html = ''
    for user in all_users:
        url = '/home/' + str(user.id) + '/'
        html += '<a href = "' + url + '">' + user.uname + '</a><br>'
    '''
    return HttpResponse(template.render(context, request))
    #return HttpResponse("<h1>this is the index fx in home</h1>")

def detail(request, user_id):
    return HttpResponse("<h2>User id: " + str(user_id) + "</h2>")
