from django.shortcuts import get_object_or_404, render

# Create your views here.

from  django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Node_Dir, Media_Dir, Node, Media_Org

def index(request):
	return render(request, 'nodanews/index.html', {})

def node_dir(request):
	return render(request, 'nodanews/node_dir.html', {})

def media_dir(request):
	return render(request, 'nodanews/media_dir.html', {})
	
def node(request, node_id):
	node = get_object_or_404(Node, pk=node_id)
	return render(request, 'nodanews/node.html', {'node': list})

def media_org(request, media_dir_id, media_org_id):
	list = get_object_or_404(Media_dir, pk=media_dir_id)
	media_org = get_object_or_404(Media_Org, pk=media_org_id)
	return render(request, 'nodanews/media_org.html', {'media_org': list})

