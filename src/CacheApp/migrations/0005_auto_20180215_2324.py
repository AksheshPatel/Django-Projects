# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-15 23:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CacheApp', '0004_auto_20180215_2322'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Word_Meaning',
            new_name='WordMeaning',
        ),
    ]
