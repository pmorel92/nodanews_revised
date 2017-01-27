from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.template import Context
from  django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import F

from .models import Node, Media_Org, Index, Link_Sources, Link_Academic, Link_Nodes, Link_Video, Link_Wikipedia

def index(request):
	index = get_object_or_404(Index)
	nodes = Node.objects.order_by('-date_posted')[0:3]
	media_orgs = Media_Org.objects.order_by('-date_posted')[0:3]
	t = get_template('nodanews/index.html')
	html = t.render(Context({'index': index, 'nodes': nodes, 'media_orgs': media_orgs}))
	return HttpResponse(html)
	
def about(request):
	return render(request, 'nodanews/about.html', {})

def node_dir(request):
	nodes = Node.objects.order_by('-date_posted')
	return render(request, 'nodanews/node_dir.html', {'nodes': nodes})	

def media_dir(request):
	media_orgs = Media_Org.objects.order_by('name')
	return render(request, 'nodanews/media_dir.html', {'media_orgs': media_orgs})

def node(request, node_id):
	node = get_object_or_404(Node, pk=node_id)
	ref = Node.id
	link_source = Link_Sources.objects.get(Link_Sources.node_ref_id=ref)
	link_wikipedia = Link_Wikipedia.objects.filter()
	link_academic = Link_Academic.objects.filter(node_id=Link_Academic.node_ref.id)
	link_node = Link_Nodes.objects.filter(node_id=Link_Nodes.node_ref.id)
	link_video = Link_Video.objects.filter(node_id=Link_Video.node_ref.id)
	return render(request, 'nodanews/node.html', {'node': node, 'link_source': link_source, 'link_wikipedia': link_wikipedia, 'link_academic': link_academic ,'link_node': link_node, 'link_video': link_node})


def media_org(request, media_org_id):
	media_org = get_object_or_404(Media_Org, pk=media_org_id)
	return render(request, 'nodanews/media_org.html', {'media_org': media_org})

