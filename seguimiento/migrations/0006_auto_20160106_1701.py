# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0005_auto_20151231_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuevapregunta',
            name='plazo',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='nuevapregunta',
            name='size',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
