# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline

from sodaseo.models import Seo, Config, Template, Url, Var
from sodaseo.forms import SeoForm, ConfigForm, TemplateForm, UrlForm, VarForm


class SeoInline(GenericStackedInline):

    model = Seo
    form = SeoForm
    max_num = 1
    fieldsets = (
        (None, {
            'fields': (
                'template', 'title', 'keywords', 'description', 'author'
            )
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


class VarInline(admin.StackedInline):

    model = Var
    form = VarForm
    extra = 1


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


class UrlAdmin(admin.ModelAdmin):

    list_display = (
        'path', 'site', 'created_at'
    )
    form = UrlForm
    search_fields = ['path', ]
    list_filter = ('site', )
    inlines = [VarInline, SeoInline]


admin.site.register(Config, ConfigAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Url, UrlAdmin)
