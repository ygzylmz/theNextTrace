# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-09-14 10:22
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20200914_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloggezi',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=5000, null=True, verbose_name='İcerik'),
        ),
    ]
