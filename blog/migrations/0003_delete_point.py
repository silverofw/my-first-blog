# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 04:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_point'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Point',
        ),
    ]
