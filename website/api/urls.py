from django.urls import path, re_path
from django.conf.urls import url
#from home.views import index
import home
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView



urlpatterns = [
        re_path(r'^$', home.views.index, name='index'),
        url(r'^v1/users/$', CreateView.as_view(), name="create"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
