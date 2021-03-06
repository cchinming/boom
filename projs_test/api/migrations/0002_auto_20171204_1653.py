# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 08:53
from __future__ import unicode_literals

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=255)),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='records',
            name='data',
            field=models.CharField(blank=True, default='', max_length=255, validators=[api.models.records.clean]),
        ),
        migrations.AlterField(
            model_name='records',
            name='host',
            field=models.CharField(blank=True, default='', max_length=255, validators=[api.models.records.validate_host]),
        ),
        migrations.AlterField(
            model_name='records',
            name='type',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('AAAA', 'AAAA'), ('CNAME', 'CNAME'), ('NS', 'NS')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='records',
            name='zone',
            field=models.CharField(blank=True, default='', max_length=255, validators=[api.models.records.validate_zone]),
        ),
    ]
