# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-07-20 06:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200717_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='post',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
