# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-25 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvindex', '0003_auto_20170225_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='runtime',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]