# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0010_auto_20160211_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualizacion',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
