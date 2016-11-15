# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_auto_20161105_0811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint_register',
            name='cr_cno',
        ),
        migrations.RemoveField(
            model_name='complaint_register',
            name='cr_rollno',
        ),
        migrations.AddField(
            model_name='complaint',
            name='c_date',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='c_status',
            field=models.CharField(choices=[('Sent', 'Sent'), ('Recieved', 'Recieved'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Sent', max_length=25),
        ),
        migrations.DeleteModel(
            name='Complaint_register',
        ),
    ]
