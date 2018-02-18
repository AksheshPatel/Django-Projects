# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class Course(models.Model):
# 	course_name = models.CharField(max_length=120)

# class Student(models.Model):
# 	student_name = models.CharField(max_length=120)
# 	course_name = models.ForeignKey(Course, on_delete=models.CASCADE)

# class Teacher(models.Model):
# 	teacher_name = models.CharField(max_length=120)
# 	course_name = models.ForeignKey(Course, on_delete=models.CASCADE)

# 	def __unicode__(self):
# 		return self.teacher_name

# 	def __str__(self):
# 		return self.teacher_name





class Student2(models.Model):
	student_name = models.CharField(max_length=120)

class Teacher2(models.Model):
	teacher_name = models.CharField(max_length=120)

	def __unicode__(self):
		return self.teacher_name

	# def __str__(self):
	# 	return self.teacher_name

class Course2(models.Model):
	course_name = models.CharField(max_length=120)
	student_name = models.ForeignKey(Student2, on_delete=models.CASCADE)
	teacher_name = models.ForeignKey(Teacher2, on_delete=models.CASCADE)




	
