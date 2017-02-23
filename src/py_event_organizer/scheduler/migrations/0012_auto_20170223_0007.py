# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0011_auto_20170223_0004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delegates',
            options={'verbose_name': 'Contact Delegates', 'verbose_name_plural': 'Delegates'},
        ),
        migrations.AlterField(
            model_name='participant',
            name='delegates',
            field=models.ManyToManyField(blank=True, related_name='related_to', through='scheduler.Delegates', to='scheduler.Participant'),
        ),
    ]
