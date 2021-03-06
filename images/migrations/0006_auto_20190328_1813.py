# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-28 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20190327_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default='User', max_length=50),
        ),
    ]
