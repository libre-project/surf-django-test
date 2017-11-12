# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 00:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', related_query_name='books', to='books.Author', verbose_name='Автор'),
        ),
    ]
