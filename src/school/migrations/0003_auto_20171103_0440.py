# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-03 04:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20171102_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='course_name',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
