# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171204_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.CharField(default='', max_length=255),
        ),
    ]
