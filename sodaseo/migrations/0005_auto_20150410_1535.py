# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodaseo', '0004_auto_20150409_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='og_type',
            field=models.CharField(blank=True, max_length=255, verbose_name='og:type', choices=[('website', 'website'), ('article', 'article')]),
            preserve_default=True,
        ),
    ]
