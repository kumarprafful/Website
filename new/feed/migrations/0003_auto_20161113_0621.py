# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20161112_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='content',
            field=models.TextField(default='Story Content Here'),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
