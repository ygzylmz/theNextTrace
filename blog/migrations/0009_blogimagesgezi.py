# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-07-16 13:04
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200701_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImagesGezi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=blog.models.upload_to, verbose_name='Image')),
                ('bloggezi', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogGezi')),
            ],
        ),
    ]
