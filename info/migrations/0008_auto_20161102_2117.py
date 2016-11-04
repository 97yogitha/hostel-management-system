# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 15:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20161101_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
