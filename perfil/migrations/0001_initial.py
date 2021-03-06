# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-01 18:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.TextField(blank=True, null=True)),
                ('lote_actual', models.CharField(blank=True, max_length=100, null=True)),
                ('desarrollo', models.CharField(blank=True, max_length=100, null=True)),
                ('pagos', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
