# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0007_auto_20160506_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='email',
            field=models.EmailField(max_length=256, null=True, blank=True),
        ),
    ]
