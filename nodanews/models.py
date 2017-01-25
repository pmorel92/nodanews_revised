from django.db import models


class Index(models.Model):
	headline = models.CharField(max_length=200, default='')
	Link_1 = models.CharField(max_length=500, default='', blank=True)
	Link_1_title = models.CharField(max_length=200, default='', blank=True)
	Link_2 = models.CharField(max_length=500, default='', blank=True)
	Link_2_title = models.CharField(max_length=200, default='', blank=True)
	Link_3 = models.CharField(max_length=500, default='', blank=True)
	Link_3_title = models.CharField(max_length=200, default='', blank=True)
	headline_2 = models.CharField(max_length=200, default='', blank=True)
	Link_21 = models.CharField(max_length=500, default='', blank=True)
	Link_21_title = models.CharField(max_length=200, default='', blank=True)
	Link_22 = models.CharField(max_length=500, default='', blank=True)
	Link_22_title = models.CharField(max_length=200, default='', blank=True)
	Link_23 = models.CharField(max_length=500, default='', blank=True)
	Link_23_title = models.CharField(max_length=200, default='', blank=True)
	headline_3 = models.CharField(max_length=200, default='', blank=True)
	Link_31 = models.CharField(max_length=500, default='', blank=True)
	Link_31_title = models.CharField(max_length=200, default='', blank=True)
	Link_32 = models.CharField(max_length=500, default='', blank=True)
	Link_32_title = models.CharField(max_length=200, default='', blank=True)
	Link_33 = models.CharField(max_length=500, default='', blank=True)
	Link_33_title = models.CharField(max_length=200, default='', blank=True)
	headline_4 = models.CharField(max_length=200, default='', blank=True)
	Link_41 = models.CharField(max_length=500, default='', blank=True)
	Link_41_title = models.CharField(max_length=200, default='', blank=True)
	Link_42 = models.CharField(max_length=500, default='', blank=True)
	Link_42_title = models.CharField(max_length=200, default='', blank=True)
	Link_43 = models.CharField(max_length=500, default='', blank=True)
	Link_43_title = models.CharField(max_length=200, default='', blank=True)
	index_image = models.ImageField(upload_to='media/index')
	
	def __str__(self):
		return self.headline
	
		
class Node(models.Model):
	headline = models.CharField(max_length=200, default='')
	subject = models.CharField(max_length=100, default='')
	country = models.CharField(max_length=100, default='')
	date_posted = models.DateTimeField()
	my_take = models.TextField()
	node_image = models.ImageField(upload_to='media/nodes')
	video_embed = models.CharField(max_length=500, default='', blank=True)
	
	def __str__(self):
		return self.headline
class Link(models.Model):
	
    SOURCES = 'Sou'
    WIKIPEDIA = 'Wik'
    VIDEO = 'Vid'
    ACADEMIC = 'Aca'
    NODE_LINKS = 'Nod'
    ATTRIBUTE_CHOICES = (
        (SOURCES, 'Sources'),
        (WIKIPEDIA, 'Wikipedia'),
        (VIDEO, 'Video'),
        (ACADEMIC, 'Academic'),
        (NODE_LINKS, 'Nodes'),
    )

    attribute = models.CharField(max_length=10,choices=ATTRIBUTE_CHOICES, default=SOURCES)
    title_1 = models.CharField(max_length=200, default='title', blank=True)
    link_url = models.CharField(max_length=500, default='url', blank=True)
    title_2 = models.CharField(max_length=200, default='title', blank=True)
    link_url_2 = models.CharField(max_length=500, default='url', blank=True)
    title_3 = models.CharField(max_length=200, default='title', blank=True)
    link_url_3 = models.CharField(max_length=500, default='url', blank=True)
    title_4 = models.CharField(max_length=200, default='title', blank=True)
    link_url_4 = models.CharField(max_length=500, default='url', blank=True)
    title_5 = models.CharField(max_length=200, default='title', blank=True)
    link_url_5 = models.CharField(max_length=500, default='url', blank=True)
    title_6 = models.CharField(max_length=200, default='title', blank=True)
    link_url_6 = models.CharField(max_length=500, default='url', blank=True)
    title_7 = models.CharField(max_length=200, default='title', blank=True)
    link_url_7 = models.CharField(max_length=500, default='url', blank=True)
    title_8 = models.CharField(max_length=200, default='title', blank=True)
    link_url_8 = models.CharField(max_length=500, default='url', blank=True)
    title_9 = models.CharField(max_length=200, default='title', blank=True)
    link_url_9 = models.CharField(max_length=500, default='url', blank=True)
    title_10 = models.CharField(max_length=200, default='title', blank=True)
    link_url_10 = models.CharField(max_length=500, default='url', blank=True)
    node = models.ForeignKey(Node)
	
    def __str__(self):
        return '{} / {}'.format(self.node.headline, self.attribute)
	
class Media_Org(models.Model):
	name = models.CharField(max_length=100, default='')
	date_posted = models.DateTimeField()
	home_page = models.CharField(max_length=200, default='')
	date_founded = models.DateField(default='1965-08-08')
	logo = models.ImageField(upload_to='media/logos')
	description = models.TextField()
	bias = models.CharField(max_length=100, default='')
	duplicate_bias = models.BooleanField(default=True)
	country = models.CharField(max_length=100, default='')
	duplicate_country = models.BooleanField(default=True)
	fake_or_not = models.BooleanField(default=False)
	
	
	def __str__(self):
		return self.name
