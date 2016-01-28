# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0003_auto_20160128_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsvp',
            name='status',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='attending',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='responded',
            field=models.BooleanField(default=False),
        ),
    ]
