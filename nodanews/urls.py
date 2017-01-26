from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^node_dir/$', views.node_dir, name='node_dir_index'),
	url(r'^media_dir/$', views.media_dir, name='media_dir_index'),
	url(r'^node_dir/(?P<node_id>[0-9]+)/$', views.node, views.node.link_dict, name='node'),
	url(r'^media_dir/(?P<media_org_id>[0-9]+)/$', views.media_org, name='media_org')
]