# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacttype',
            name='abbreviation',
        ),
        migrations.RemoveField(
            model_name='contacttype',
            name='name',
        ),
        migrations.AddField(
            model_name='contacttype',
            name='type',
            field=models.CharField(choices=[('SMS', 'Text Message'), ('EMAIL', 'Email')], default='SMS', max_length=5),
        ),
    ]
