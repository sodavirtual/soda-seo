# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline

from sodaseo.models import Seo, Config, Template
from sodaseo.forms import SeoForm, ConfigForm, TemplateForm


class SeoInline(GenericStackedInline):

    model = Seo
    form = SeoForm
    max_num = 1
    fieldsets = (
        (None, {
            'fields': ('title', 'keywords', 'description', 'author')
        }),
        ('Open Graph', {
            'fields': (
                'og_site_name', 'og_title', 'og_type', 'og_image', 'og_url',
                'og_description', 'article_published_time',
                'article_modified_time', 'article_section', 'article_tag'
            )
        }),
        ('Google+', {
            'fields': (
                'itemprop_name', 'itemprop_description', 'itemprop_image'
            )
        }),
        ('Twitter Card', {
            'fields': (
                'twitter_card', 'twitter_site', 'twitter_title',
                'twitter_description', 'twitter_image', 'twitter_url'
            )
        }),
    )


class ConfigAdmin(admin.ModelAdmin):

    list_display = (
        'site_name', 'google_site_verification', 'fb_appid', 'site',
        'created_at'
    )
    list_filter = ('site', )
    form = ConfigForm
    search_fields = ['site_name', ]
    inlines = [SeoInline, ]


class TemplateAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'created_at'
    )
    form = TemplateForm
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Config, ConfigAdmin)
admin.site.register(Template, TemplateAdmin)
