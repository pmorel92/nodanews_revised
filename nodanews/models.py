from django.db import models

class Node_Dir(models.Model):
    name = models.CharField(max_length=100, default='')
    
    def __str__(self):
	    return self.name
		
class Node(models.Model):
    headline = models.CharField(max_length=200, default='')
    subject = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    date_posted = models.DateTimeField()
    my_take = models.TextField()
    head_image = models.ImageField(upload_to='media/nodes', default='')
    foot_image = models.ImageField(upload_to='media/nodes', default='')
    video_embed1 = models.CharField(max_length=500, default='', blank=True)
    video_embed2 = models.CharField(max_length=500, default='', blank=True)
    video_embed3 = models.CharField(max_length=500, default='', blank=True)    
    hotness = models.IntegerField(default=1)
    node_direc = models.ForeignKey(Node_Dir)

	
    def __str__(self):
	    return self.headline      

class Perspective(models.Model):
    name = models.CharField(max_length=47, default='')
    node = models.ForeignKey(Node)
    
    def __str__(self):
	    return "{}/{}".format(self.node, self.name)
	    
class Link(models.Model):
	link_title = models.CharField(max_length=90, default='', blank=True)
	link_url = models.CharField(max_length=300, default='', blank=True)
	link_media = models.CharField(max_length=21, default='', blank=True)
	link_media_url = models.CharField(max_length=300, default="", blank=True)
	perspective = models.ForeignKey(Perspective)
	
	def __str__(self):
	    return "{}/{}".format(self.link_title, self.perspective)
	    
class Media_Org(models.Model):
	name = models.CharField(max_length=100, default='')
	date_posted = models.DateTimeField()
	home_page = models.CharField(max_length=200, default='')
	date_founded = models.DateField(default='1965-08-08')
	logo = models.ImageField(upload_to='media/logos')
	description = models.TextField()
	fake_or_not = models.BooleanField(default=False)
	ready = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name
