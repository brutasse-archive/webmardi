from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.cheese_list, name='cheese_list'),
    url(r'^cheese/(?P<pk>\d+)/$', views.cheese_detail, name='cheese_detail'),
    url(r'^cheese/(?P<pk>\d+)/like/$', views.like_cheese, name='like_cheese'),
    url(r'^cheese/(?P<pk>\d+)/dislike/$', views.dislike_cheese, name='dislike_cheese'),

    url(r'^cheese/add/$', views.add_cheese, name='add_cheese'),
)
