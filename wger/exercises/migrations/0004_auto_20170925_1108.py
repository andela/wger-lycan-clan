# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-25 08:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0003_auto_20160921_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='equipment',
            field=models.ManyToManyField(blank=True, to='exercises.Equipment', verbose_name='Equipment'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='muscles',
            field=models.ManyToManyField(blank=True, to='exercises.Muscle', verbose_name='Primary muscles'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='muscles_secondary',
            field=models.ManyToManyField(blank=True, related_name='secondary_muscles', to='exercises.Muscle', verbose_name='Secondary muscles'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='status',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'Accepted'), ('3', 'Declined')], default='1', editable=False, max_length=2),
        ),
        migrations.AlterField(
            model_name='exerciseimage',
            name='is_main',
            field=models.BooleanField(default=False, help_text='Tick the box if you want to set this image as the main one for the exercise (will be shown e.g. in the search). The first image is automatically marked by the system.', verbose_name='Main picture'),
        ),
        migrations.AlterField(
            model_name='exerciseimage',
            name='status',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'Accepted'), ('3', 'Declined')], default='1', editable=False, max_length=2),
        ),
    ]
