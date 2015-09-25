# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline
from django.conf import settings

from sodaseo.models import Seo, Config, Template, Url, Var
from sodaseo.forms import SeoForm, ConfigForm, TemplateForm, UrlForm, VarForm
from sodaseo.settings import SODA_SEO_I18N


class SeoAllInline(GenericStackedInline):

    model = Seo
    form = SeoForm
    max_num = 1
    extra = 0

    fieldsets = (
        (None, {
            'fields': (
                'language',
                'template',
                'title',
                'description',
                'keywords',
                'author',
                'image',
            )
        }),
        ('Open Graph', {
            'fields': (
                'og_site_name',
                # 'og_title',
                'og_type',
                # 'og_image',
                # 'og_video',
                # 'og_audio',
                # 'og_description',
                'og_see_also',
                # 'article_published_time',
                # 'article_modified_time',
                # 'article_section',
                # 'article_author',
                # 'article_publisher',
                # 'article_tag'
            )
        }),
        ('Google+', {
            'fields': (
                'itemscope_itemtype',
                # 'itemprop_name',
                # 'itemprop_description',
                # 'itemprop_image'
            )
        }),
        ('Twitter Card', {
            'fields': (
                # 'twitter_site',
                # 'twitter_title',
                # 'twitter_description',
                'twitter_creator',
                # 'twitter_image'
            )
        }),
    )

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = self.max_num

        if SODA_SEO_I18N:
            max_num = len(settings.LANGUAGES)

        return max_num


class SeoInline(SeoAllInline):

    max_num = 1
    extra = 0

    fieldsets = (
        (None, {
            'fields': (
                'language',
                'template',
                'title',
                'description',
                'keywords',
                'author',
                'image',
            )
        }),
        ('Open Graph', {
            'fields': (
                # 'og_site_name',
                # 'og_title',
                'og_type',
                # 'og_image',
                # 'og_video',
                # 'og_audio',
                # 'og_description',
                'og_see_also',
                'article_published_time',
                # 'article_modified_time',
                'article_section',
                'article_author',
                'article_publisher',
                'article_tag'
            )
        }),
        ('Google+', {
            'fields': (
                'itemscope_itemtype',
                # 'itemprop_name',
                # 'itemprop_description',
                # 'itemprop_image'
            )
        }),
        ('Twitter Card', {
            'fields': (
                # 'twitter_site',
                # 'twitter_title',
                # 'twitter_description',
                'twitter_creator',
                # 'twitter_image'
            )
        }),
    )


class SeoUrlInline(SeoAllInline):

    fieldsets = (
        (None, {
            'fields': (
                'language',
                'template',
                'title',
                'description',
                'keywords',
                'author',
                'image',
            )
        }),
        ('Open Graph', {
            'fields': (
                # 'og_site_name',
                # 'og_title',
                'og_type',
                # 'og_image',
                # 'og_video',
                # 'og_audio',
                # 'og_description',
                'og_see_also',
                # 'article_published_time',
                # 'article_modified_time',
                # 'article_section',
                # 'article_author',
                # 'article_publisher',
                # 'article_tag'
            )
        }),
        ('Google+', {
            'fields': (
                'itemscope_itemtype',
                # 'itemprop_name',
                # 'itemprop_description',
                # 'itemprop_image'
            )
        }),
        ('Twitter Card', {
            'fields': (
                # 'twitter_site',
                # 'twitter_title',
                # 'twitter_description',
                'twitter_creator',
                # 'twitter_image'
            )
        }),
    )


class VarInline(admin.StackedInline):

    model = Var
    form = VarForm
    extra = 1


class ConfigAdmin(admin.ModelAdmin):

    list_display = (
        'site_name', 'google_site_verification', 'fb_appid', 'fb_profile_id',
        'site', 'created_at'
    )
    list_filter = ('site', )
    form = ConfigForm
    search_fields = ['site_name', ]
    inlines = [SeoAllInline, ]


class TemplateAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'created_at'
    )
    form = TemplateForm
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name',)}


class UrlAdmin(admin.ModelAdmin):

    list_display = (
        'path', 'site', 'created_at'
    )
    form = UrlForm
    search_fields = ['path', ]
    list_filter = ('site', )
    inlines = [SeoUrlInline, ]


admin.site.register(Config, ConfigAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Url, UrlAdmin)
