from django.urls import path, re_path
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

urlpatterns = [
        re_path(r'^$', views.index, name='index'),
        re_path(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail' ),
        url(r'^users/$', CreateView.as_view(), name="create"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
