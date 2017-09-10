from __future__ import unicode_literals

from django.db import models


# Create your models here.
class profiles(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(null=True)
	location = models.CharField(max_length=120, default="my location")
	job = models.CharField(max_length=120, null=True)

	def __unicode__(self):
		return self.name