# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_auto_20170222_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='type',
            field=models.CharField(choices=[('SMS', 'Text Message'), ('EMAIL', 'Email')], default='SMS', max_length=3),
        ),
    ]
