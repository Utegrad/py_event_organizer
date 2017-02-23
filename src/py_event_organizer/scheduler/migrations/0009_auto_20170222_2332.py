# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 06:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0008_auto_20170222_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(choices=[('EDIT', 'Editor'), ('VIEW', 'Viewer')], default='EDIT', max_length=4)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Organization')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Participant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(through='scheduler.Membership', to='scheduler.Participant'),
        ),
    ]
