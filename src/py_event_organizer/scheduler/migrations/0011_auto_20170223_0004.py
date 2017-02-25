# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 07:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_auto_20170222_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delegates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('delegate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delegated_to', to='scheduler.Participant')),
                ('organizaton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Organization')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delegated_from', to='scheduler.Participant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='participant',
            name='delegates',
            field=models.ManyToManyField(related_name='related_to', through='scheduler.Delegates', to='scheduler.Participant'),
        ),
    ]