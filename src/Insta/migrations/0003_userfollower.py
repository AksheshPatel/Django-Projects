# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-10 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0002_auto_20171109_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userfollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insta.Userdetail')),
            ],
        ),
    ]
