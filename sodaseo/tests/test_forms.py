from django.test import TestCase
from django.contrib.sites.models import Site

from sodaseo.forms import UrlForm, ConfigForm


class TestUrlForm(TestCase):

    def test_clean_path(self):
        site = Site.objects.get_current()
        site2 = Site.objects.create(name='example2.com', domain='example2.com')

        form = UrlForm(
            {'site': site.pk, 'path': '/'}
        )
        self.assertTrue(form.is_valid())
        form.save()

        form = UrlForm(
            {'site': site.pk, 'path': '/'}
        )
        self.assertFalse(form.is_valid())
        errors = dict(form.errors)
        self.assertIn('Url já cadastrada.', errors['path'])

        form = UrlForm(
            {'site': site2.pk, 'path': '/'}
        )
        self.assertTrue(form.is_valid())
        form.save()


class TestConfigForm(TestCase):

    def test_clean_site(self):
        site = Site.objects.get_current()

        form = ConfigForm(
            {'site': site.pk, 'site_name': 'Site'}
        )
        self.assertTrue(form.is_valid())
        form.save()

        form = ConfigForm(
            {'site': site.pk, 'site_name': 'Site'}
        )
        self.assertFalse(form.is_valid())
        errors = dict(form.errors)
        self.assertIn(
            'Já existe uma configuração para esse site.', errors['site']
        )
