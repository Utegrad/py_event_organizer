# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0009_auto_20170222_2332'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('participant', 'organization')]),
        ),
    ]
