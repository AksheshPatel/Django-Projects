# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Course2,Student2,Teacher2

# admin.site.register(Course)
# admin.site.register(Student)
# admin.site.register(Teacher)
admin.site.register(Course2)
admin.site.register(Student2)
admin.site.register(Teacher2)