# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodaseo', '0002_auto_20150401_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='description',
            field=models.TextField(verbose_name='descri\xe7\xe3o', blank=True),
            preserve_default=True,
        ),
    ]
