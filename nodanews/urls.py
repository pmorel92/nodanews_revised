from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^node_dir/$', views.node_dir, name='node_dir_index'),
	url(r'^node_dir/(?P<node_dir_subject>)/$', views.node_dir_subject, name='node_dir_subject'),
	#testing
	#url(r'^node_dir/(?P<node_dir_country>/$', views.node_dir_country, name='node_dir_country'),
	url(r'^media_dir/$', views.media_dir, name='media_dir_index'),
	#url(r'^media_dir/(?P<media_dir_bias>)/$', views.media_dir_bias, name='media_dir_bias',
	#url(r'^media_dir/(?P<media_dir_country>)/$' views.media_dir_country, name='media_dir_country',
	url(r'^nodes/(?P<node_id>[0-9]+)/$', views.node, name='node'),
	url(r'^media_orgs/(?P<media_org_id>[0-9]+)/$', views.media_org, name='media_org')
]