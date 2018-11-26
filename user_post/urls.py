from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.main, name = 'main'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.show_post, name = 'show_post'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^posts/add_likes/(?P<post_id>\d+)/$', views.addlikes, name = 'addlikes'),
    url(r'^posts/add_dislike/(?P<post_id>\d+)/$', views.dislike, name = 'dislike'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    ]
