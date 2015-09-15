# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodaseo', '0008_auto_20150721_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='google_analytics_id',
            field=models.CharField(max_length=255, verbose_name='google-analytics-id', blank=True),
        ),
    ]
