# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodaseo', '0005_auto_20150410_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='seo',
            name='itemscope_itemtype',
            field=models.CharField(blank=True, max_length=255, verbose_name='itemscope itemtype', choices=[('http://schema.org/Article', 'Article'), ('http://schema.org/Blog', 'Blog'), ('http://schema.org/Book', 'Book'), ('http://schema.org/Event', 'Event'), ('http://schema.org/LocalBusiness', 'LocalBusiness'), ('http://schema.org/Organization', 'Organization'), ('http://schema.org/Person', 'Person'), ('http://schema.org/Product', 'Product'), ('http://schema.org/Review', 'Review'), ('http://schema.org/Other', 'Other'), ('http://schema.org/WebSite', 'WebSite')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='description',
            field=models.TextField(verbose_name='instru\xe7\xf5es de ajuda', blank=True),
            preserve_default=True,
        ),
    ]
