# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20160629_1713'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
