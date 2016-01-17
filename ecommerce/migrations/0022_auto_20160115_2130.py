# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-15 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0021_choicelabel_choiceoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicelabel',
            name='icon',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='choicelabel',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='choiceoption',
            name='icon',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='choiceoption',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]