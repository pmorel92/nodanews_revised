# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 23:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0012_auto_20170127_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link_academic',
            old_name='node_ref',
            new_name='node',
        ),
        migrations.RenameField(
            model_name='link_nodes',
            old_name='node_ref',
            new_name='node',
        ),
        migrations.RenameField(
            model_name='link_sources',
            old_name='node_ref',
            new_name='node',
        ),
        migrations.RenameField(
            model_name='link_video',
            old_name='node_ref',
            new_name='node',
        ),
        migrations.RenameField(
            model_name='link_wikipedia',
            old_name='node_ref',
            new_name='node',
        ),
    ]