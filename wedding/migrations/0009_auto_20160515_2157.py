# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-15 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0008_auto_20160509_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='confirmed_party_size',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='party_size',
            field=models.IntegerField(default=2),
        ),
    ]
