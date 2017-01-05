from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.template.loader import get_template
from django.template import Context
from  django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Node_Dir, Media_Dir, Node, Media_Org, Index

def index(request):
	index = get_object_or_404(Index)
	t = get_template('nodanews/index.html')
	html = t.render(Context({'index': index}))
	return HttpResponse(html)

def node_dir(request):
	nodes = Node.objects.order_by('date_posted')
	return render(request, 'nodanews/node_dir.html', {'nodes': nodes})

def node_dir_subject(request, node_dir_subject):
	node_dir_subject = Node_Dir.objects.get(Node_Dir, pk=node_dir_subject)
	return render(request, 'nodanews/node_dir.html', {'node_dir_subject': node_dir_subject})
	
def about(request):
	return render(request, 'nodanews/about.html', {})	

def media_dir(request):
	media_orgs = Media_Org.objects.order_by('name')
	return render(request, 'nodanews/media_dir.html', {'media_orgs': media_orgs})
	
def node(request, node_id):
	node = get_object_or_404(Node, pk=node_id)
	return render(request, 'nodanews/node.html', {'node': node})

def media_org(request, media_org_id):
	media_org = get_object_or_404(Media_Org, pk=media_org_id)
	return render(request, 'nodanews/media_org.html', {'media_org': media_org})

