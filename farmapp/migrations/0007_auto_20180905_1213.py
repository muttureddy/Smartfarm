# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-05 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0006_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmapp.County'),
        ),
    ]
