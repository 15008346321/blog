# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-07 12:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='atype',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
