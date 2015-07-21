# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodaseo', '0006_auto_20150413_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='seo',
            name='language',
            field=models.CharField(db_index=True, max_length=10, verbose_name='Idioma', blank=True),
            preserve_default=True,
        ),
    ]
