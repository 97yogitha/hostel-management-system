# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 09:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0017_complaint_c_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='c_date',
        ),
    ]
