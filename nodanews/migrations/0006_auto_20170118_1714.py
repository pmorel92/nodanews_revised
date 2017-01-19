# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0005_auto_20170118_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='index_image',
            field=models.ImageField(upload_to='/images/index'),
        ),
        migrations.AlterField(
            model_name='media_org',
            name='logo',
            field=models.ImageField(upload_to='/images/logos'),
        ),
        migrations.AlterField(
            model_name='node',
            name='node_image',
            field=models.ImageField(upload_to='/images/nodes'),
        ),
    ]
