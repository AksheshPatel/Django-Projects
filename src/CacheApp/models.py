from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Word(models.Model):
	word_name = models.CharField(max_length=120)
	word_meaning = models.CharField(max_length=120,null=True)
	
	def __unicode__(self):
		return self.word_name