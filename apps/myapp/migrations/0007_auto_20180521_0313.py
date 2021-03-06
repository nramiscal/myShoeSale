# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-21 03:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20180521_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_buyer', to='myapp.User'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_product', to='myapp.Product'),
        ),
    ]
