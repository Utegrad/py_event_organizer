# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0018_auto_20170224_2036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='name',
            new_name='full_name',
        ),
        migrations.AddField(
            model_name='participant',
            name='first_name',
            field=models.CharField(default='value', max_length=48),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='last_name',
            field=models.CharField(default='lastName', max_length=48),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='nick_name',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
