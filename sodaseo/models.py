# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

import os
from filer.fields.image import FilerImageField


class CreateUpdateModel(models.Model):

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Config(CreateUpdateModel):

    site = models.ForeignKey(
        Site,
        verbose_name='site',
        related_name='sodaseo_config',
        default=settings.SITE_ID
    )

    site_name = models.CharField(
        'site_name',
        max_length=255
    )

    google_site_verification = models.CharField(
        'google-site-verification',
        max_length=255,
        blank=True
    )

    fb_appid = models.CharField(
        'fb:app_id',
        max_length=255,
        blank=True
    )

    fb_profile_id = models.CharField(
        'fb:profile_id',
        max_length=255,
        blank=True
    )

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'configuração'
        verbose_name_plural = 'configurações'

    def to_dict(self):
        data = {
            'site_name': self.site_name,
            'google_site_verification': self.google_site_verification,
            'fb_appid': self.fb_appid,
            'fb_profile_id': self.fb_profile_id
        }

        return data


@python_2_unicode_compatible
class Template(CreateUpdateModel):

    name = models.CharField(
        'nome',
        max_length=255
    )

    slug = models.SlugField(
        'identificador',
        max_length=255,
        unique=True
    )

    body = models.TextField(
        'conteúdo'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'template'
        verbose_name_plural = 'templates'
        ordering = ['name']


@python_2_unicode_compatible
class Url(CreateUpdateModel):

    site = models.ForeignKey(
        Site,
        verbose_name='site',
        related_name='sodaseo_urls',
        default=settings.SITE_ID
    )

    path = models.CharField(
        'caminho',
        max_length=255
    )

    description = models.TextField(
        'descrição',
        blank=True
    )

    def __str__(self):
        return self.path

    class Meta:
        verbose_name = 'url'
        verbose_name_plural = 'urls'
        ordering = ['path']
        unique_together = ('site', 'path')


@python_2_unicode_compatible
class Var(CreateUpdateModel):

    url = models.ForeignKey(
        Url,
        verbose_name='url',
        related_name='vars',
    )

    name = models.CharField(
        'nome',
        max_length=255
    )

    description = models.TextField(
        'descrição'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'variável'
        verbose_name_plural = 'variáveis'
        ordering = ['name']


@python_2_unicode_compatible
class Seo(CreateUpdateModel):

    template = models.ForeignKey(
        'Template',
        verbose_name='template'
    )

    # base
    title = models.CharField(
        'title',
        max_length=255
    )

    keywords = models.CharField(
        'keywords',
        max_length=255,
        blank=True
    )

    description = models.CharField(
        'description',
        max_length=255
    )

    author = models.CharField(
        'author',
        max_length=255,
        blank=True
    )

    # opengraph
    og_site_name = models.CharField(
        'og:site_name',
        max_length=255,
        blank=True
    )

    og_title = models.CharField(
        'og:title',
        max_length=255,
        blank=True
    )

    og_type = models.CharField(
        'og:type',
        max_length=255,
        blank=True
    )

    og_image = FilerImageField(
        null=True,
        blank=True,
        verbose_name='og:image',
        on_delete=models.SET_NULL,
        related_name='seo_og_image'
    )

    og_video = models.URLField(
        'og:video',
        max_length=255,
        blank=True
    )

    og_audio = models.URLField(
        'og:audio',
        max_length=255,
        blank=True
    )

    og_url = models.CharField(
        'og:url',
        max_length=255,
        blank=True
    )

    og_description = models.CharField(
        'og:description',
        max_length=255,
        blank=True
    )

    og_see_also = models.TextField(
        'og:see_also',
        blank=True
    )

    article_published_time = models.DateTimeField(
        'article:published_time',
        blank=True,
        null=True
    )

    article_modified_time = models.DateTimeField(
        'article:modified_time',
        blank=True,
        null=True
    )

    article_section = models.CharField(
        'article:section',
        max_length=255,
        blank=True
    )

    article_author = models.CharField(
        'article:author',
        max_length=255,
        blank=True
    )

    article_publisher = models.CharField(
        'article:publisher',
        max_length=255,
        blank=True
    )

    article_tag = models.CharField(
        'article:tag',
        max_length=255,
        blank=True
    )

    # google+
    itemprop_name = models.CharField(
        'itemprop=name',
        max_length=255,
        blank=True
    )

    itemprop_description = models.CharField(
        'itemprop=description',
        max_length=255,
        blank=True
    )

    itemprop_image = FilerImageField(
        null=True,
        blank=True,
        verbose_name='itemprop=image',
        on_delete=models.SET_NULL,
        related_name='seo_itemprop_image'
    )

    # twitter
    twitter_card = models.CharField(
        'twitter:card',
        max_length=255,
        blank=True
    )

    twitter_site = models.CharField(
        'twitter:site',
        max_length=255,
        blank=True
    )

    twitter_title = models.CharField(
        'twitter:title',
        max_length=255,
        blank=True
    )

    twitter_description = models.CharField(
        'twitter:description',
        max_length=255,
        blank=True
    )

    twitter_creator = models.CharField(
        'twitter:creator',
        max_length=255,
        blank=True
    )

    twitter_image = FilerImageField(
        null=True,
        blank=True,
        verbose_name='twitter:image',
        on_delete=models.SET_NULL,
        related_name='seo_twitter_image'
    )

    # generic relation
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'entrada seo'
        verbose_name_plural = 'entradas seo'

    def to_dict(self):
        fields = (
            'template',
            'title',
            'keywords',
            'description',
            'author',
            'og_site_name',
            'og_title',
            'og_type',
            'og_image',
            'og_video',
            'og_audio',
            'og_url',
            'og_description',
            'og_see_also',
            'article_published_time',
            'article_modified_time',
            'article_section',
            'article_author',
            'article_publisher',
            'article_tag',
            'itemprop_name',
            'itemprop_description',
            'itemprop_image',
            'twitter_card',
            'twitter_site',
            'twitter_title',
            'twitter_description',
            'twitter_creator',
            'twitter_image',
            'content_object'
        )

        data = {}

        for field in fields:
            try:
                if getattr(self, field):
                    data[field] = getattr(self, field)
            except:
                pass

        return data


def get_default_template():
    import sodaseo
    template_dir = os.path.join(
        os.path.dirname(sodaseo.__file__), 'templates/sodaseo/default.html'
    )
    f = open(template_dir)
    return f.read()
