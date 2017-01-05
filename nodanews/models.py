from django.db import models


class Index(models.Model):
	headline = models.CharField(max_length=200, default='')
	Link_1 = models.CharField(max_length=500, default='', blank=True)
	Link_1_title = models.CharField(max_length=200, default='', blank=True)
	Link_2 = models.CharField(max_length=500, default='', blank=True)
	Link_2_title = models.CharField(max_length=200, default='', blank=True)
	Link_3 = models.CharField(max_length=500, default='', blank=True)
	Link_3_title = models.CharField(max_length=200, default='', blank=True)
	Link_4 = models.CharField(max_length=500, default='', blank=True)
	Link_4_title = models.CharField(max_length=200, default='', blank=True)
	Link_5 = models.CharField(max_length=500, default='', blank=True)
	Link_5_title = models.CharField(max_length=200, default='', blank=True)
	
	def __str__(self):
		return self.headline
	
class Node_Dir(models.Model):
	title = models.CharField(max_length=100, default='country/subject')
	subject = models.CharField(max_length=100, default='')
	country = models.CharField(max_length=100, default='')

	def __str__(self):
		return self.title
	
class Media_Dir(models.Model):
	title = models.CharField(max_length=100, default='country/bias')
	bias = models.CharField(max_length=100, default='')	
	country = models.CharField(max_length=100, default='')
	
	def __str__(self):
		return self.title
		
class Node(models.Model):
	headline = models.CharField(max_length=200, default='')
	date_posted = models.DateTimeField()
	my_take = models.TextField()
	node_image = models.ImageField(upload_to='nodanews/static/images/nodes')
	Link_1 = models.CharField(max_length=500, default='', blank=True)
	Link_1_title = models.CharField(max_length=200, default='', blank=True)
	Link_2 = models.CharField(max_length=500, default='', blank=True)
	Link_2_title = models.CharField(max_length=200, default='', blank=True)
	Link_3 = models.CharField(max_length=500, default='', blank=True)
	Link_3_title = models.CharField(max_length=200, default='', blank=True)
	Link_4 = models.CharField(max_length=500, default='', blank=True)
	Link_4_title = models.CharField(max_length=200, default='', blank=True)
	Link_5 = models.CharField(max_length=500, default='', blank=True)
	Link_5_title = models.CharField(max_length=200, default='', blank=True)
	Link_6 = models.CharField(max_length=500, default='', blank=True)
	Link_6_title = models.CharField(max_length=200, default='', blank=True)
	Link_7 = models.CharField(max_length=500, default='', blank=True)
	Link_7_title = models.CharField(max_length=200, default='', blank=True)
	Link_8 = models.CharField(max_length=500, default='', blank=True)
	Link_8_title = models.CharField(max_length=200, default='', blank=True)
	Link_9 = models.CharField(max_length=500, default='', blank=True)
	Link_9_title = models.CharField(max_length=200, default='', blank=True)
	Link_10 = models.CharField(max_length=500, default='', blank=True)
	Link_10_title = models.CharField(max_length=200, default='', blank=True)
	node_dir = models.ForeignKey(Node_Dir)
	
	def __str__(self):
		return self.headline

class Media_Org(models.Model):
	name = models.CharField(max_length=100, default='')
	home_page = models.CharField(max_length=200, default='')
	date_founded = models.DateField()
	logo = models.ImageField(upload_to='nodanews/static/images/logos')
	description = models.TextField()
	media_dir = models.ForeignKey(Media_Dir)
	fake_or_not = models.BooleanField()
	
	def __str__(self):
		return self.name
