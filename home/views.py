from django.shortcuts import render
from django.http import Http404
from rest_framework import generics
from .serializers import UsersSerializer
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


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
