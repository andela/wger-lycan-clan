# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-25 08:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0006_auto_20170925_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]