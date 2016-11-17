from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	created = models.DateTimeField(default=timezone.now)
	published = models.DateTimeField(blank=True, null=True)

	def publish(self):
		if not self.published:
			self.published = timezone.now()
			self.save()

	def __str__(self):
		return self.title

