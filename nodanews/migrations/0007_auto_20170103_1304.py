# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-03 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0006_auto_20170103_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(default='', max_length=200)),
                ('Link_1', models.CharField(blank=True, default='', max_length=500)),
                ('Link_1_title', models.CharField(blank=True, default='', max_length=200)),
                ('Link_2', models.CharField(blank=True, default='', max_length=500)),
                ('Link_2_title', models.CharField(blank=True, default='', max_length=200)),
                ('Link_3', models.CharField(blank=True, default='', max_length=500)),
                ('Link_3_title', models.CharField(blank=True, default='', max_length=200)),
                ('Link_4', models.CharField(blank=True, default='', max_length=500)),
                ('Link_4_title', models.CharField(blank=True, default='', max_length=200)),
                ('Link_5', models.CharField(blank=True, default='', max_length=500)),
                ('Link_5_title', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='media_dir',
            old_name='title',
            new_name='bias',
        ),
        migrations.RenameField(
            model_name='node_dir',
            old_name='title',
            new_name='subject',
        ),
        migrations.RemoveField(
            model_name='media_dir',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='node_dir',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='node',
            name='Link_10',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_10_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_3',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_3_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_4',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_4_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_5',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_5_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_6',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_6_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_7',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_7_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_8',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_8_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_9',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='node',
            name='Link_9_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='media_org',
            name='date_founded',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='node',
            name='Link_1',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='node',
            name='Link_1_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='node',
            name='Link_2',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='node',
            name='Link_2_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
