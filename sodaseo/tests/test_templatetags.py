from django.contrib.sites.models import Site
from django.template import Template as DjangoTemplate
from django.template import Context
from django.test import RequestFactory, TestCase

from sodaseo.models import Config, Seo, Template, Url, get_default_template


class TestSodaSeoRenderTags(TestCase):
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
            description='My Awesome Site Description.', og_see_also='test'
        )
        self.config_seo.content_object = self.config
        self.config_seo.save()

    def test_render_tag(self):
        request = self.factory.get('/')
        t = DjangoTemplate(
            '{% load sodaseo_tags %}{% sodaseo_render_tags site_id=1 %}'
        )
        ctx = Context({'request': request})
        data = t.render(ctx)
        self.assertIn('<title>My Awesome Site.</title>', data)
        self.assertIn(
            '<meta name="description" content="My Awesome Site Description.">',
            data
        )

    def test_render_tag_with_url(self):
        url = Url.objects.create(site=self.site, path='/')
        url_seo = Seo(
            template=self.template, title='My Site.',
            description='My Description.'
        )
        url_seo.content_object = url
        url_seo.save()
        request = self.factory.get('/')
        t = DjangoTemplate(
            '{% load sodaseo_tags %}{% sodaseo_render_tags site_id=1 %}'
        )
        ctx = Context({'request': request})
        data = t.render(ctx)
        self.assertIn('<title>My Site.</title>', data)
        self.assertIn(
            '<meta name="description" content="My Description.">',
            data
        )


class TestSodaSeoRenderAnalytics(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.site = Site.objects.get_current()
        self.template = Template.objects.create(
            name='Default', slug='default', body=get_default_template()
        )
        self.config = Config.objects.create(
            site=self.site, site_name='My Site', google_analytics_id='HUEHUEBR'
        )
        self.config_seo = Seo(
            template=self.template, title='My Awesome Site.',
            description='My Awesome Site Description.'
        )
        self.config_seo.content_object = self.config
        self.config_seo.save()

    def test_render_tag(self):
        request = self.factory.get('/')
        t = DjangoTemplate(
            '{% load sodaseo_tags %}{% sodaseo_render_analytics %}'
        )
        ctx = Context({'request': request})
        data = t.render(ctx)
        self.assertIn('HUEHUEBR', data)

    def test_render_tag_without_config(self):
        self.config.delete()
        request = self.factory.get('/')
        t = DjangoTemplate(
            '{% load sodaseo_tags %}{% sodaseo_render_analytics %}'
        )
        ctx = Context({'request': request})
        data = t.render(ctx)
        self.assertIn('', data)


class TestSodaSeoRenderExtraHead(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.site = Site.objects.get_current()
        self.template = Template.objects.create(
            name='Default', slug='default', body=get_default_template()
        )
        self.config = Config.objects.create(
            site=self.site, site_name='My Site', extra_head='HUEHUEBR'
        )
        self.config_seo = Seo(
            template=self.template, title='My Awesome Site.',
            description='My Awesome Site Description.'
        )
        self.config_seo.content_object = self.config
        self.config_seo.save()

    def test_render_tag(self):
        request = self.factory.get('/')
        t = DjangoTemplate(
            '{% load sodaseo_tags %}{% sodaseo_render_extra_head %}'
        )
        ctx = Context({'request': request})
        data = t.render(ctx)
        self.assertIn('HUEHUEBR', data)

    def test_render_tag_without_config(self):
        self.config.delete()
        request = self.factory.get('/')
        t = DjangoTemplate(
            '{% load sodaseo_tags %}{% sodaseo_render_extra_head %}'
        )
        ctx = Context({'request': request})
        data = t.render(ctx)
        self.assertIn('', data)


class TestSodaSeoRenderExtraBody(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.site = Site.objects.get_current()
        self.template = Template.objects.create(
            name='Default', slug='default', body=get_default_template()
        )
        self.config = Config.objects.create(
            site=self.site, site_name='My Site', extra_body='HUEHUEBR'
        )
        self.config_seo = Seo(
            template=self.template, title='My Awesome Site.',
            description='My Awesome Site Description.'
        )
        self.config_seo.content_object = self.config
        self.config_seo.save()

    def test_render_tag(self):
        request = self.factory.get('/')
        t = DjangoTemplate(
            '{% load sodaseo_tags %}{% sodaseo_render_extra_body %}'
        )
        ctx = Context({'request': request})
        data = t.render(ctx)
        self.assertIn('HUEHUEBR', data)

    def test_render_tag_without_config(self):
        self.config.delete()
        request = self.factory.get('/')
        t = DjangoTemplate(
            '{% load sodaseo_tags %}{% sodaseo_render_extra_body %}'
        )
        ctx = Context({'request': request})
        data = t.render(ctx)
        self.assertIn('', data)
