# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0016_remove_complaint_c_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='c_date',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
