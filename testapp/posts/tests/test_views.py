# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.urls import reverse
from django.contrib.sites.models import Site

from model_mommy import mommy

from sodaseo.models import Config, Template, Url, Seo, get_default_template
from posts.models import Post


class TestPostList(TestCase):

    def test_render(self):
        site = Site.objects.get_current()
        template = Template.objects.create(
            name='default', slug='default', body=get_default_template()
        )
        config = Config.objects.create(
            site_name='Site Name', site=site,
            google_analytics_id='UA-00000000-0'
        )
        Seo.objects.create(
            content_object=config,
            title='Site Name - {{ sodaseo.site_name }}',
            template=template
        )
        mommy.make(Post, _quantity=5)
        url = reverse('post_list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 5)
        self.assertContains(
            response, '<title>Site Name - Site Name</title>'
        )
        self.assertContains(response, 'UA-00000000-0')

        url_obj = Url.objects.create(
            site=site, path='/posts/'
        )
        Seo.objects.create(
            content_object=url_obj,
            title='Post List - {{ sodaseo.site_name }}',
            template=template
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 5)
        self.assertContains(
            response, '<title>Post List - Site Name</title>'
        )


class TestPostDetail(TestCase):

    def test_render(self):
        site = Site.objects.get_current()
        template = Template.objects.create(
            name='default', slug='default', body=get_default_template()
        )
        config = Config.objects.create(
            site_name='Site Name', site=site
        )
        Seo.objects.create(
            content_object=config,
            title='Site Name - {{ sodaseo.site_name }}',
            template=template
        )
        post = mommy.make(Post)
        url = reverse('post_detail', args=[post.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], post)
        self.assertContains(
            response, '<title>Site Name - Site Name</title>'
        )

        url_obj = Url.objects.create(
            site=site, path='/posts/{0}/'.format(post.pk)
        )
        Seo.objects.create(
            content_object=url_obj,
            title='Post Detail - {{ sodaseo.site_name }}',
            template=template
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], post)
        self.assertContains(
            response, '<title>Post Detail - Site Name</title>'
        )

        Seo.objects.create(
            content_object=post,
            title='Post Detail 2 - {{ sodaseo.site_name }}',
            template=template
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], post)
        self.assertContains(
            response, '<title>Post Detail 2 - Site Name</title>'
        )


class TestRenderTagsDetail(TestCase):

    def setUp(self):
        self.url = reverse('render_tags_detail')

    def test_render(self):
        site = Site.objects.get_current()
        template = Template.objects.create(
            name='default', slug='default', body=get_default_template()
        )
        config = Config.objects.create(
            site_name='Site Name', site=site
        )
        Seo.objects.create(
            content_object=config,
            title='Index - {{ sodaseo.site_name }}',
            template=template
        )
        url_obj = Url.objects.create(
            site=site, path='/sodaseo-render-tags/'
        )
        Seo.objects.create(
            content_object=url_obj,
            title='Render Tags - {{ sodaseo.site_name }}',
            template=template
        )

        response = self.client.get(self.url)
        self.assertContains(response, 'Index - Site Name')

        response = self.client.get(self.url, {'url': '/sodaseo-render-tags/'})
        self.assertContains(response, 'Render Tags - Site Name')
