# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_remove_hostel_office_dept_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
                ('morning', models.TextField()),
                ('afternoon', models.TextField()),
                ('snacks', models.TextField()),
                ('dinner', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='mess',
            name='afternoon',
        ),
        migrations.RemoveField(
            model_name='mess',
            name='day',
        ),
        migrations.RemoveField(
            model_name='mess',
            name='dinner',
        ),
        migrations.RemoveField(
            model_name='mess',
            name='morning',
        ),
        migrations.RemoveField(
            model_name='mess',
            name='snacks',
        ),
        migrations.AddField(
            model_name='messmenu',
            name='mess_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Mess'),
        ),
    ]
