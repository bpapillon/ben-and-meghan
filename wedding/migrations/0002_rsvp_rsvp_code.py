# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='rsvp_code',
            field=models.CharField(default=None, unique=True, max_length=128, db_index=True),
            preserve_default=False,
        ),
    ]
