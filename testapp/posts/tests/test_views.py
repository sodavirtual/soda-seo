# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.core.urlresolvers import reverse
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
            site_name='Site Name', site=site
        )
        Seo.objects.create(
            content_object=config,
            title='Site Name',
            template=template
        )
        mommy.make(Post, _quantity=5)
        url = reverse('post_list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 5)
        self.assertContains(
            response, '<title>Site Name</title>'
        )

        url_obj = Url.objects.create(
            site=site, path='/posts/'
        )
        Seo.objects.create(
            content_object=url_obj,
            title='Post List',
            template=template
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 5)
        self.assertContains(
            response, '<title>Post List</title>'
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
            title='Site Name',
            template=template
        )
        post = mommy.make(Post)
        url = reverse('post_detail', args=[post.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], post)
        self.assertContains(
            response, '<title>Site Name</title>'
        )

        url_obj = Url.objects.create(
            site=site, path='/posts/{0}/'.format(post.pk)
        )
        Seo.objects.create(
            content_object=url_obj,
            title='Post Detail',
            template=template
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], post)
        self.assertContains(
            response, '<title>Post Detail</title>'
        )

        Seo.objects.create(
            content_object=post,
            title='Post Detail 2',
            template=template
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], post)
        self.assertContains(
            response, '<title>Post Detail 2</title>'
        )
