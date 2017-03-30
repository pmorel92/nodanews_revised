from django.contrib import admin

from .models import Node, Media_Org, Link, Perspective, Node_Dir


class Node_Admin(admin.ModelAdmin):
    fieldsets = [
	    (None, {
		    'fields': ('headline', 'subject', 'country', 'date_posted', 'my_take', 'head_image', 'foot_image' 'video_embed1', 'video_embed2', 'video_embed3', 'ready', 'hotness', 'node_direc')
        }),
        ]
    ordering = ('-date_posted',)
        
        
class Media_Org_Admin(admin.ModelAdmin):
	fieldsets = [

	
	]

admin.site.register(Node, Node_Admin)
admin.site.register(Node_Dir)
admin.site.register(Link)
admin.site.register(Perspective)
admin.site.register(Media_Org, Media_Org_Admin)

