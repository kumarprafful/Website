from django.db import models
from datetime import date
from django.utils.translation import gettext as _
from django.core.urlresolvers import reverse


class story(models.Model):
	author = models.CharField(max_length=250)
	story_title = models.CharField(max_length=250)
	date = models.DateField(_("Date"), default=date.today)
	genre = models.CharField(max_length=100)
	story_logo = models.FileField()
	content = models.TextField(max_length=15000)
	likes = models.PositiveIntegerField(default=0)
	
	def get_absolute_url(self):
		return reverse('feed:read', kwargs={'pk': self.pk}) 


	def __str__(self):
		return self.story_title

class comment(models.Model):
	story = models.ForeignKey(story, related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.name,self.story)

