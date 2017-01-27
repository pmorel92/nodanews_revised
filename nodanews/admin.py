from django.contrib import admin

# Register your models here.
from .models import Node, Media_Org, Index, Link_Sources, Link_Academic, Link_Nodes, Link_Video, Link_Wikipedia


class Node_Admin(admin.ModelAdmin):
	fieldsets = [
 
	]
class Media_Org_Admin(admin.ModelAdmin):
	fieldsets = [

	
	]

class Index_Admin(admin.ModelAdmin):
	fieldsets = [

	
	]	
class Link_Sources_Admin(admin.ModelAdmin):
	fieldsets = [

	
	]	
class Link_Wikipedia_Admin(admin.ModelAdmin):
	fieldsets = [

	
	]		
class Link_Academic_Admin(admin.ModelAdmin):
	fieldsets = [

	
	]
class Link_Nodes_Admin(admin.ModelAdmin):
	fieldsets = [

	
	]	
class Link_Video_Admin(admin.ModelAdmin):
	fieldsets = [

	
	]		
admin.site.register(Node, Node_Admin)
admin.site.register(Media_Org, Media_Org_Admin)
admin.site.register(Index, Index_Admin)
admin.site.register(Link_Sources, Link_Sources_Admin)
admin.site.register(Link_Wikipedia, Link_Wikipedia_Admin)
admin.site.register(Link_Academic, Link_Academic_Admin)
admin.site.register(Link_Nodes, Link_Nodes_Admin)
admin.site.register(Link_Video, Link_Video_Admin)