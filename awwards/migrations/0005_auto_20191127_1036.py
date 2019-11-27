# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-27 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0004_auto_20191125_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='upload_date',
        ),
        migrations.AddField(
            model_name='project',
            name='upload_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awwards.Profile'),
        ),
    ]
