# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0014_auto_20170223_0013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delegates',
            old_name='organizaton',
            new_name='organization',
        ),
        migrations.AlterUniqueTogether(
            name='delegates',
            unique_together=set([('participant', 'delegate'), ('participant', 'delegate', 'organization')]),
        ),
    ]
