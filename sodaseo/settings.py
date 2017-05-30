from django.conf import settings


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
