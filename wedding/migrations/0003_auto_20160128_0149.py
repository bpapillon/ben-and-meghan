# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0002_rsvp_rsvp_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsvp',
            name='attending',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'Invited'), (1, b'Attending'), (2, b'Not Attending')]),
        ),
    ]
