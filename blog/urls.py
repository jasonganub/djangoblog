from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
)
