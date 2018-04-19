from django.contrib.sites.models import Site
from django.test import RequestFactory, TestCase
from django.utils.encoding import smart_text
from model_mommy import mommy

from sodaseo.models import (Config, Seo, Template, Url, Var,
                            get_default_template, get_sodaseo_context)


class TestConfig(TestCase):
    def test_create_model(self):
        config = mommy.make(Config)
        self.assertEqual(smart_text(config), config.site_name)
        data = config.to_dict()
        self.assertTrue(data)


class TestTemplate(TestCase):
    def test_create_model(self):
        template = mommy.make(Template)
        self.assertEqual(smart_text(template), template.name)


class TestUrl(TestCase):
    def test_create_model(self):
        url = mommy.make(Url)
        self.assertEqual(smart_text(url), url.path)


class TestVar(TestCase):
    def test_create_model(self):
        var = mommy.make(Var)
        self.assertEqual(smart_text(var), var.name)


class TestSeo(TestCase):
    def test_create_model(self):
        seo = mommy.make(Seo)
        self.assertEqual(smart_text(seo), seo.title)
        data = seo.to_dict()
        self.assertTrue(data)


class TestGetDefaultTemplate(TestCase):
    def test_function(self):
        data = get_default_template()
        self.assertTrue(data)


class TestGetSodaSeoContext(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.site = Site.objects.get_current()
        self.template = Template.objects.create(
            name='Default', slug='default', body=get_default_template()
        )
        self.config = Config.objects.create(
            site=self.site, site_name='My Site'
        )
        self.config_seo = Seo(
            template=self.template, title='My Awesome Site.',
            description='My Awesome Site Description.'
        )
        self.config_seo.content_object = self.config
        self.config_seo.save()
        self.url = Url.objects.create(site=self.site, path='/')
        self.url_seo = Seo(
            template=self.template, title='Welcome to my site.',
            description='Welcome to my site description.'
        )
        self.url_seo.content_object = self.url
        self.url_seo.save()

    def test_without_language(self):
        request = self.factory.get('/')

        data = get_sodaseo_context(request, site_id=self.site.pk)
        self.assertEqual(data['title'], 'Welcome to my site.')
        self.assertEqual(
            data['description'], 'Welcome to my site description.'
        )
        self.url_seo.delete()
        self.url.delete()

        data = get_sodaseo_context(request, site_id=self.site.pk)
        self.assertEqual(data['title'], 'My Awesome Site.')
        self.assertEqual(data['description'], 'My Awesome Site Description.')

    def test_with_language(self):
        config_seo_with_language = Seo(
            template=self.template, title='Meu site.',
            description='Meu site - descrição.', language='pt-br'
        )
        config_seo_with_language.content_object = self.config
        config_seo_with_language.save()
        url_seo_with_language = Seo(
            template=self.template, title='Bem vindo ao site.',
            description='Bem vindo ao site - descrição.', language='pt-br'
        )
        url_seo_with_language.content_object = self.url
        url_seo_with_language.save()
        request = self.factory.get('/')

        data = get_sodaseo_context(request, site_id=self.site.pk)
        self.assertEqual(data['title'], 'Bem vindo ao site.')
        self.assertEqual(
            data['description'], 'Bem vindo ao site - descrição.'
        )
        self.url_seo.delete()
        url_seo_with_language.delete()
        self.url.delete()

        data = get_sodaseo_context(request, site_id=self.site.pk)
        self.assertEqual(data['title'], 'Meu site.')
        self.assertEqual(
            data['description'], 'Meu site - descrição.'
        )
