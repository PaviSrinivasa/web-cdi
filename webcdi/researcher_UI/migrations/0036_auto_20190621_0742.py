# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-21 07:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('researcher_UI', '0035_auto_20190602_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='benchmark',
            old_name='percentile_boy',
            new_name='raw_score_boy',
        ),
        migrations.RenameField(
            model_name='benchmark',
            old_name='percentile_girl',
            new_name='raw_score_girl',
        ),
    ]
