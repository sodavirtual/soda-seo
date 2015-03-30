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
