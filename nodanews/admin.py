from django.contrib import admin

# Register your models here.
from .models import Node, Media_Org, Index


class Node_Admin(admin.ModelAdmin):
    fieldsets = [
	    (None, {
		    'fields': ('headline', 'subject', 'country', 'date_posted', 'my_take', 'node_image', 'video_embed')
        }),
        ('Sources Links', {
            'classes': ('collapse',),
            'fields': ('sources_title_1', 'sources_link_url', 'sources_title_2', 'sources_link_url_2', 'sources_title_3', 'sources_link_url_3', 'sources_title_4', 'sources_link_url_4', 'sources_title_5', 'sources_link_url_5', 'sources_title_6', 'sources_link_url_6', 'sources_title_7', 'sources_link_url_7', 'sources_title_8', 'sources_link_url_8', 'sources_title_9', 'sources_link_url_9', 'sources_title_10', 'sources_link_url_10'),
        }),
        ('Wikipedia Links', {
            'classes': ('collapse',),
			'fields': ('wikipedia_title_1', 'wikipedia_link_url', 'wikipedia_title_2', 'wikipedia_link_url_2', 'wikipedia_title_3', 'wikipedia_link_url_3', 'wikipedia_title_4', 'wikipedia_link_url_4', 'wikipedia_title_5', 'wikipedia_link_url_5', 'wikipedia_title_6', 'wikipedia_link_url_6', 'wikipedia_title_7', 'wikipedia_link_url_7', 'wikipedia_title_8', 'wikipedia_link_url_8', 'wikipedia_title_9', 'wikipedia_link_url_9', 'wikipedia_title_10', 'wikipedia_link_url_10'),
        }),	
        ('Academic Links', {
            'classes': ('collapse',),
			'fields': ('academic_title_1', 'academic_link_url', 'academic_title_2', 'academic_link_url_2', 'academic_title_3', 'academic_link_url_3', 'academic_title_4', 'academic_link_url_4', 'academic_title_5', 'academic_link_url_5', 'academic_title_6', 'academic_link_url_6', 'academic_title_7', 'academic_link_url_7', 'academic_title_8', 'academic_link_url_8', 'academic_title_9', 'academic_link_url_9', 'academic_title_10', 'academic_link_url_10'),
        }),
        ('Nodes Links', {
            'classes': ('collapse',),
			'fields': ('nodes_title_1', 'nodes_link_url', 'nodes_title_2', 'nodes_link_url_2', 'nodes_title_3', 'nodes_link_url_3', 'nodes_title_4', 'nodes_link_url_4', 'nodes_title_5', 'nodes_link_url_5', 'nodes_title_6', 'nodes_link_url_6', 'nodes_title_7', 'nodes_link_url_7', 'nodes_title_8', 'nodes_link_url_8', 'nodes_title_9', 'nodes_link_url_9', 'nodes_title_10', 'nodes_link_url_10'),
        }),
        ('Video Links', {
            'classes': ('collapse',),
			'fields': ('video_title_1', 'video_link_url', 'video_title_2', 'video_link_url_2', 'video_title_3', 'video_link_url_3', 'video_title_4', 'video_link_url_4', 'video_title_5', 'video_link_url_5', 'video_title_6', 'video_link_url_6', 'video_title_7', 'video_link_url_7', 'video_title_8', 'video_link_url_8', 'video_title_9', 'video_link_url_9', 'video_title_10', 'video_link_url_10'),
        }),		
    ]
class Media_Org_Admin(admin.ModelAdmin):
	fieldsets = [
	    (None, {
	        'fields': ('index_image', 'headline', 'headline_2', 'headline_3', 'headline_4')       
	    }),
        ('Links', {
            'classes': ('collapse'),
            'fields': ('link_1', 'link_1_title', 'link_2', 'link_2_title', 'link_3', 'link_3_title', 'link_4')
        }),
        ('Links', {
            'classes': ('collapse'),
            'fields': ('link_21', 'link_21_title', 'link_22', 'link_22_title', 'link_23', 'link_23_title', 'link_24')
        }),
        ('Links', {
            'classes': ('collapse'),
            'fields': ('link_31', 'link_31_title', 'link_32', 'link_32_title', 'link_33', 'link_33_title', 'link_34')
        }),
        ('Links', {
            'classes': ('collapse'),
            'fields': ('link_41', 'link_41_title', 'link_42', 'link_42_title', 'link_43', 'link_43_title', 'link_44')
        }),

	
	]

class Index_Admin(admin.ModelAdmin):
	fieldsets = [

	
	]	
		
admin.site.register(Node, Node_Admin)
admin.site.register(Media_Org, Media_Org_Admin)
admin.site.register(Index, Index_Admin)