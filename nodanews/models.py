from django.db import models

class Node_Dir(models.Model):
	date_posted = models.DateTimeField()
	title = models.CharField(max_length=100, default='')
	country = models.CharField(max_length=100, default='')

	def __str__(self):
		return self.title
	
class Media_Dir(models.Model):
	date_posted = models.DateTimeField()
	title = models.CharField(max_length=100, default='')	
	country = models.CharField(max_length=100, default='')
	
	def __str__(self):
		return self.title
		
class Node(models.Model):
	title = models.CharField(max_length=100, default='')
	headline = models.CharField(max_length=200, default='')
	date_posted = models.DateTimeField()
	my_take = models.TextField()
	node_image = models.ImageField(upload_to='images')
	Link_1 = models.CharField(max_length=500, default='')
	Link_1_title = models.CharField(max_length=200, default='')
	Link_2 = models.CharField(max_length=500, default='')
	Link_2_title = models.CharField(max_length=200, default='')
	node_dir = models.ForeignKey(Node_Dir)
	
	def __str__(self):
		return self.title

class Media_Org(models.Model):
	name = models.CharField(max_length=100, default='')
	date_founded = models.DateTimeField()
	logo = models.ImageField(upload_to='images/logos')
	description = models.TextField()
	media_dir = models.ForeignKey(Media_Dir)
	
	def __str__(self):
		return self.name
