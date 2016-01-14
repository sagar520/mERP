# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-14 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0018_auto_20160114_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amountPaid',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
