# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-16 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CacheApp', '0008_delete_mean'),
    ]

    operations = [
        migrations.CreateModel(
            name='Findmeaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wn', models.CharField(max_length=120)),
                ('wm', models.CharField(max_length=120)),
            ],
        ),
    ]
