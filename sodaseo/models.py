# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from filer.fields.image import FilerImageField


class CreateUpdateModel(models.Model):

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True


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

    def __unicode__(self):
        return self.site_name

    class Meta:
        verbose_name = 'configuração'
        verbose_name_plural = 'configurações'


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

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'template'
        verbose_name_plural = 'templates'
        ordering = ['name']


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

    def __unicode__(self):
        return self.path

    class Meta:
        verbose_name = 'url'
        verbose_name_plural = 'urls'
        ordering = ['path']
        unique_together = ('site', 'path')


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

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'variável'
        verbose_name_plural = 'variáveis'
        ordering = ['name']


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
        max_length=255,
        blank=True
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

    twitter_image = FilerImageField(
        null=True,
        blank=True,
        verbose_name='twitter:image',
        on_delete=models.SET_NULL,
        related_name='seo_twitter_image'
    )

    twitter_url = models.CharField(
        'twitter:url',
        max_length=255,
        blank=True
    )

    # generic relation
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'entrada seo'
        verbose_name_plural = 'entradas seo'
