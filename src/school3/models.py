# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Course22(models.Model):
	course_name = models.CharField(max_length=120)

	def __unicode__(self):
		return self.course_name

class Student22(models.Model):
	student_name = models.CharField(max_length=120)
	course_name = models.ForeignKey(Course22, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.student_name

class Student3(models.Model):
	student_name = models.CharField(max_length=120)
	course_name = models.ManyToManyField(Course22)

	def __unicode__(self):
		return self.student_name

class Teacher22(models.Model):
	teacher_name = models.CharField(max_length=120)
	course_name = models.ForeignKey(Course22, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.teacher_name

class Teacher3(models.Model):
	teacher_name = models.CharField(max_length=120)
	course_name = models.ManyToManyField(Course22)

	def __unicode__(self):
		return self.teacher_name

	

	# def __str__(self):
	# 	return self.teacher_name
