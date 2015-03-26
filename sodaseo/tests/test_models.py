# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.utils.encoding import smart_text

from model_mommy import mommy

from sodaseo.models import Config, Template, Url, Var, Seo


class TestConfig(TestCase):

    def test_create_model(self):
        config = mommy.make(Config)
        self.assertEqual(smart_text(config), config.site_name)


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
