# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 00:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0022_auto_20170318_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]