# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-10-14 18:45
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20200914_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdizi',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=10000, null=True, verbose_name='İcerik'),
        ),
        migrations.AlterField(
            model_name='blogfilm',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=10000, null=True, verbose_name='İcerik'),
        ),
        migrations.AlterField(
            model_name='bloggezi',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=10000, null=True, verbose_name='İcerik'),
        ),
        migrations.AlterField(
            model_name='bloghayat',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=10000, null=True, verbose_name='İcerik'),
        ),
    ]
