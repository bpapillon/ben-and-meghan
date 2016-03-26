# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0004_auto_20160128_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsvp',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='last_name',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='name',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rsvp',
            name='rsvp_code_slug',
            field=models.CharField(default=None, unique=True, max_length=128, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rsvp',
            name='staying_friday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='staying_onsite',
            field=models.BooleanField(default=False),
        ),
    ]
