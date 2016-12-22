# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-20 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0002_auto_20161219_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node_dir',
            name='current',
        ),
        migrations.AddField(
            model_name='node_dir',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='media_org',
            name='logo',
            field=models.ImageField(upload_to='images/logos'),
        ),
        migrations.AlterField(
            model_name='node',
            name='node_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
