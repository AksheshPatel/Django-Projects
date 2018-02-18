# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-15 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CacheApp', '0002_auto_20180215_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word_Meaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_meaning', models.CharField(max_length=120)),
                ('word_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_meaning',
        ),
    ]
