# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodaseo', '0007_seo_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seo',
            options={'ordering': ('created_at',), 'verbose_name': 'entrada seo', 'verbose_name_plural': 'entradas seo'},
        ),
    ]
