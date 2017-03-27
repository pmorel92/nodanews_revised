from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.template import Context
from  django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import F

from .models import Node, Media_Org, Perspective, Link, Node_Dir

def index(request, node_id, media_org_id):
	nodes = Node.objects.order_by('-date_posted')
	media_orgs = Media_Org.objects.all()
	return render(request, 'nodanews/index.html', {'nodes': nodes}, {'media_orgs': media_orgs})
	
def about(request):
	return render(request, 'nodanews/about.html', {})

def node_dir(request):
	nodes = Node.objects.order_by('headline')
	return render(request, 'nodanews/node_dir.html', {'nodes': nodes})	

def media_dir(request):
	media_orgs = Media_Org.objects.order_by('name')
	return render(request, 'nodanews/media_dir.html', {'media_orgs': media_orgs})

def node(request, node_id, perspective_id):
	node = get_object_or_404(Node, pk=node_id)
	perspective = get_object_or_404(Perspective, pk=node_id)
	links = get_object_or_404(Link, pk=perspective_id)
	return render(request, 'nodanews/node.html', {'node': node}, {'perspective': perspective}, {'links': link})


def media_org(request, media_org_id):
	media_org = get_object_or_404(Media_Org, pk=media_org_id)
	return render(request, 'nodanews/media_org.html', {'media_org': media_org})

