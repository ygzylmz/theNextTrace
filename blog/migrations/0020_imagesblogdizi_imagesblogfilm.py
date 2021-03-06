# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-09-06 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200720_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesBlogDizi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('unique_id', models.CharField(editable=False, max_length=100, null=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogDizi')),
            ],
            options={
                'verbose_name_plural': 'ImagesGonderilerDizi',
            },
        ),
        migrations.CreateModel(
            name='ImagesBlogFilm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('unique_id', models.CharField(editable=False, max_length=100, null=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogFilm')),
            ],
            options={
                'verbose_name_plural': 'ImagesGonderilerFilm',
            },
        ),
    ]
