# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20170222_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='contact_point',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='email',
            name='type',
            field=models.CharField(choices=[('SMS', 'Text Message'), ('EMAIL', 'Email')], default='EMAIL', max_length=5),
        ),
    ]
