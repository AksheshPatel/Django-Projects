# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-10 23:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Insta', '0003_userfollower'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfollower',
            name='oriuser',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
