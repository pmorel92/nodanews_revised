from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^node_dir/$', views.node_dir, name='node_dir'),
	url(r'^media_dir/$', views.media_dir, name='media_dir'),
	url(r'^nodes/(?P<node_id>[0-9]+)/$', views.node, name='node'),
	url(r'^media_orgs/(?P<media_org_id>[0-9]+)/$', views.media_org, name='media_org')
]