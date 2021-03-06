# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-24 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2500)),
                ('link', models.CharField(max_length=2000)),
                ('upload_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
