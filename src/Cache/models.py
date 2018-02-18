from __future__ import unicode_literals

from django.db import models

# Create your models here.

class WordName(models.Model):
	word_name = models.CharField(max_length=120)
	
	def __unicode__(self):
		return self.word_name

class WordMeaning(models.Model):
	w_name = models.CharField(max_length=120)
	w_meaning = models.CharField(max_length=120)
	
	def __unicode__(self):
		return self.w_name