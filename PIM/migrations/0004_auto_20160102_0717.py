# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PIM', '0003_auto_20160102_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='source',
            field=models.TextField(max_length=1000000, null=True),
        ),
    ]
