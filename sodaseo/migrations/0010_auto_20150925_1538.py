# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('sodaseo', '0009_config_google_analytics_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='extra_body',
            field=models.TextField(verbose_name='extra body', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='config',
            name='extra_head',
            field=models.TextField(verbose_name='extra head', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seo',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='seo_image', on_delete=django.db.models.deletion.SET_NULL, verbose_name='image', blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
    ]
