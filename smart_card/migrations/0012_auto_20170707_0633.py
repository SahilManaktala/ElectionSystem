# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-07 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_card', '0011_auto_20170704_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='dob',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='net_person_id',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=8),
        ),
    ]
