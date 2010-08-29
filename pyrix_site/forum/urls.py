from django.conf.urls.defaults import *
from forum import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='forum_index'),
    url(r'^forum/(?P<forum_slug>\w+)/$', views.forum, name='forum_forum'),
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='forum_topic'),
    url(r'^topic/new/(?P<forum_id>\d+)/$', views.new_post, name='forum_new_topic'),
    url(r'^reply/new/(?P<topic_id>\d+)/$', views.new_post, name='forum_new_replay'),
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='forum_post'),
    url(r'^post/(?P<post_id>\d+)/edit/$', views.edit_post, name='forum_post_edit'),
    url(r'^user/(?P<user_id>\d+)/topics/$', views.user_topics, name='forum_user_topics'),
    url(r'^user/(?P<user_id>\d+)/posts/$', views.user_posts, name='forum_user_posts'),
    url('^markitup_preview/$', views.markitup_preview, name='markitup_preview'),
)
