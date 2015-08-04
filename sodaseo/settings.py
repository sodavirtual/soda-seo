# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings


SODA_SEO_URLS = getattr(
    settings,
    'SODA_SEO_URLS',
    (
        ('/', '/ - Página inicial'),
    )
)

SODA_SEO_I18N = getattr(
    settings,
    'SODA_SEO_I18N',
    False
)

SODA_SEO_LANGUAGES = getattr(
    settings,
    'SODA_SEO_LANGUAGES',
    settings.LANGUAGES
)
