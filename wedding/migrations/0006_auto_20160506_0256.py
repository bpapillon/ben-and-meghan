# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0005_auto_20160326_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('to', models.EmailField(max_length=256)),
                ('subject', models.CharField(max_length=256, blank=True)),
                ('body_html', models.TextField(blank=True)),
                ('body_text', models.TextField(blank=True)),
                ('sent_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='rsvp',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='updated_date',
            field=models.DateTimeField(null=True),
        ),
    ]
