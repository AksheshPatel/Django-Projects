# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Userpost,Userdetail

admin.site.register(Userpost)
admin.site.register(Userdetail)
