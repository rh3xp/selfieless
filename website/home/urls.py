from django.urls import path, re_path
from django.conf.urls import url
from . import views


urlpatterns = [
        re_path(r'^$', views.index, name='index'),
        re_path(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail' ),
        # should be api/v1/users/
        #url(r'^users/$', CreateView.as_view(), name="create"),
]

