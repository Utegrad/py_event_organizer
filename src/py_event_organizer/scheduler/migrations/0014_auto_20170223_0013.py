# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0013_auto_20170223_0009'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='delegates',
            unique_together=set([('participant', 'delegate', 'organizaton'), ('participant', 'delegate')]),
        ),
    ]
