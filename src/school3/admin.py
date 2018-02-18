# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Course22,Student22,Teacher22,Teacher3,Student3

# admin.site.register(Course)
# admin.site.register(Student)
# admin.site.register(Teacher)
admin.site.register(Course22)
admin.site.register(Student22)
admin.site.register(Student3)
admin.site.register(Teacher22)
admin.site.register(Teacher3)