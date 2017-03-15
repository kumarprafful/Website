from django.conf.urls import url
from . import views


app_name = 'feed'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
   #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='read'),
	url(r'^(?P<pk>[0-9]+)/$', views.story_detail, name='read'),
	url(r'^(?P<pk>[0-9]+)/like/$', views.story_like, name='like'),
	url(r'publish/$', views.AddStory.as_view(), name='story-publish'),
	url(r'^(?P<pk>[0-9]+)/edit/$', views.StoryUpdate.as_view(), name='story-edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.StoryDelete.as_view(), name='story-delete'),
	#comment
    #url(r'^(?P<pk>[0-9]+)/$', views.comment, name='comment'),


	url(r'^about/$', views.about, name='about'),
	url(r'^profile/$', views.profile, name='profile'),

]

