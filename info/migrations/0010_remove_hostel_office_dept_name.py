# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 08:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_auto_20161102_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostel_office',
            name='dept_name',
        ),
    ]