from django.contrib import admin

# Register your models here.
from .models import Node, Media_Org, Index


class Node_Admin(admin.ModelAdmin):
	fieldsets = [
 
	]
class Media_Org_Admin(admin.ModelAdmin):
	fieldsets = [

	
	]

class Index_Admin(admin.ModelAdmin):
	fieldsets = [

	
	]	
	

admin.site.register(Node, Node_Admin)
admin.site.register(Media_Org, Media_Org_Admin)
admin.site.register(Index, Index_Admin)