# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-25 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_auto_20170925_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='user',
        ),
    ]
