# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-03 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0005_auto_20170103_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media_org',
            name='logo',
            field=models.ImageField(upload_to='nodanews/static/images/logos'),
        ),
    ]
