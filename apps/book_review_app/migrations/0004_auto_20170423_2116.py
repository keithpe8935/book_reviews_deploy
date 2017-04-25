# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 21:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_review_app', '0003_delete_bookmanager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book_review_app.Book'),
            preserve_default=False,
        ),
    ]