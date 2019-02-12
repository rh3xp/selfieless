from django.urls import path, re_path
from . import views


urlpatterns = [
        re_path(r'^$', views.index, name='index'),
        re_path(r'^(?P<user_id>[0-9]+)/$', views.profile, name='profile' ),
]
