# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 22:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0008_auto_20170123_1721'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
    ]