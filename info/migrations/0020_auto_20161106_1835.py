# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 13:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0019_auto_20161106_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='hostel_block',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.Hostel_block'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='c_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 6, 13, 5, 11, 358901, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mess',
            name='mess_name',
            field=models.CharField(choices=[('IH', 'girls hostel top mess'), ('GH', 'girls hostel down mess'), ('MM', 'Mega mess'), ('FB', 'First Block mess'), ('SB', 'Second Block mess'), ('TB', 'Third Block mess')], max_length=25, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='messmenu',
            name='day',
            field=models.DateField(default=datetime.datetime(2016, 11, 6, 13, 5, 11, 356170, tzinfo=utc)),
        ),
    ]
