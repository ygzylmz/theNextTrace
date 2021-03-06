# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-06-27 17:45
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='default/ohdintropng.png', help_text='Kapak Fotosu Yukleyiniz', null=True, upload_to=blog.models.upload_to, verbose_name='Foto'),
        ),
    ]
