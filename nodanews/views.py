from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import F
from .models import Node, Media_Org, Perspective, Link, Node_Dir

def index(request):
	node = Node.objects.order_by('-date_posted')[0:5]
	return render(request, 'nodanews/index.html', {'node': node})
	
def about(request):
	return render(request, 'nodanews/about.html', {})

def node_dir(request):
	node_dir = Node_Dir.objects.order_by('name')
	return render(request, 'nodanews/node_dir.html', {'node_dir': node_dir})

def node_dir_part(request, node_dir_id):
	node_dir = get_object_or_404(Node_Dir, pk=node_dir_id)
	node = Node.objects.filter(node_direc__id = node_dir_id)
	return render(request, 'nodanews/node_dir.html', {'node': node})	

def media_dir(request):
	media_orgs = Media_Org.objects.order_by('name')
	return render(request, 'nodanews/media_dir.html', {'media_orgs': media_orgs})

def node(request, node_id):
	node = get_object_or_404(Node, pk=node_id)
	perspectives = Perspective.objects.filter( node__id = node_id )
	perspective_links = {
		p: Link.objects.filter(perspective__id = p.id) for p in perspectives
	}
	return render(request, 'nodanews/node.html', {'node': node, 'perspectives': perspective_links})
	
def media_org(request, media_org_id):
	media_org = get_object_or_404(Media_Org, pk=media_org_id)
	return render(request, 'nodanews/media_org.html', {'media_org': media_org})	