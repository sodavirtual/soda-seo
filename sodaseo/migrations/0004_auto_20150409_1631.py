# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodaseo', '0003_url_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='fb_profile_id',
            field=models.CharField(max_length=255, verbose_name='fb:profile_id', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seo',
            name='article_author',
            field=models.CharField(max_length=255, verbose_name='article:author', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seo',
            name='article_publisher',
            field=models.CharField(max_length=255, verbose_name='article:publisher', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seo',
            name='og_audio',
            field=models.URLField(max_length=255, verbose_name='og:audio', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seo',
            name='og_see_also',
            field=models.TextField(verbose_name='og:see_also', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seo',
            name='og_video',
            field=models.URLField(max_length=255, verbose_name='og:video', blank=True),
            preserve_default=True,
        ),
    ]
