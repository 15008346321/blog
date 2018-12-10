# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-07 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'a_type',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='is_delete',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='atype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backweb.Atype'),
        ),
    ]
