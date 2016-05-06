# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0006_auto_20160506_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='rsvp_code',
            field=models.CharField(db_index=True, max_length=128, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='rsvp_code_slug',
            field=models.CharField(db_index=True, max_length=128, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='updated_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
