# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-08 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_story_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='content',
            field=models.TextField(max_length=15000),
        ),
    ]