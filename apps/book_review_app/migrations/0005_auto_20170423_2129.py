# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_review_app', '0004_auto_20170423_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book_review_app.Author'),
            preserve_default=False,
        ),
    ]