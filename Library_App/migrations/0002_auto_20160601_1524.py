# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reader',
            old_name='grop_number',
            new_name='group_number',
        ),
        migrations.RemoveField(
            model_name='author',
            name='book_copy',
        ),
        migrations.AlterField(
            model_name='operation',
            name='operation_type',
            field=models.CharField(max_length=15),
        ),
    ]
