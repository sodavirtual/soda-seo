# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from django.contrib.sites.models import Site
from django.template import Context, Template
from django.contrib.contenttypes.models import ContentType
from django.utils import translation

from sodaseo.models import Config, Url, Seo, get_default_template
from sodaseo.utils import convert_url


register = template.Library()


@register.simple_tag(takes_context=True)
def sodaseo_render_tags(context, site_id=1):
    request = context['request']
    language_code = translation.get_language()

    # load site
    try:
        site = Site.objects.get(pk=site_id)
    except Site.DoesNotExist:
        return ''

    # load config
    config = None
    config_sodaseo = {}
    url = None
    url_sodaseo = {}

    if Config.objects.filter(site=site).exists():
        config = Config.objects.get(site=site)

    if config:
        has_config_seo = Seo.objects.filter(
            content_type=ContentType.objects.get_for_model(Config),
            object_id=config.pk
        ).exists()
        has_config_seo_with_language = Seo.objects.filter(
            content_type=ContentType.objects.get_for_model(Config),
            object_id=config.pk,
            language=language_code
        ).exists()

        if has_config_seo_with_language:
            config_sodaseo = Seo.objects.filter(
                content_type=ContentType.objects.get_for_model(Config),
                object_id=config.pk,
                language=language_code
            )[0].to_dict()
        elif has_config_seo:
            config_sodaseo = Seo.objects.filter(
                content_type=ContentType.objects.get_for_model(Config),
                object_id=config.pk
            )[0].to_dict()

        config_sodaseo.update(config.to_dict())

    has_url = Url.objects.filter(
        site=site,
        path=convert_url(request.get_full_path())
    ).exists()

    if has_url:
        url = Url.objects.get(
            site=site,
            path=convert_url(request.get_full_path())
        )
        has_url_seo = Seo.objects.filter(
            content_type=ContentType.objects.get_for_model(Url),
            object_id=url.pk
        ).exists()
        has_url_seo_with_language = Seo.objects.filter(
            content_type=ContentType.objects.get_for_model(Url),
            object_id=url.pk,
            language=language_code
        ).exists()

        if has_url_seo_with_language:
            url_sodaseo = Seo.objects.filter(
                content_type=ContentType.objects.get_for_model(Url),
                object_id=url.pk,
                language=language_code
            )[0].to_dict()
        elif has_url_seo:
            url_sodaseo = Seo.objects.filter(
                content_type=ContentType.objects.get_for_model(Url),
                object_id=url.pk
            )[0].to_dict()

    # load sodaseo from context
    sodaseo_ctx = context.get('sodaseo', {})

    # template
    template = ''

    if config_sodaseo:
        try:
            template = config_sodaseo['template'].body
        except KeyError:
            pass

    if url_sodaseo:
        try:
            template = url_sodaseo['template'].body
        except KeyError:
            pass

    if sodaseo_ctx:
        try:
            template = sodaseo_ctx['template'].body
        except KeyError:
            pass

    # create sodaseo object
    config_sodaseo.update(url_sodaseo)
    config_sodaseo.update(sodaseo_ctx)

    try:
        t = Template(template)
        context.update({'sodaseo': config_sodaseo})
        c = Context(context)
        return t.render(c)
    except:
        t = Template(get_default_template())
        context.update({'sodaseo': config_sodaseo})
        c = Context(context)
        return t.render(c)

    return ''


@register.simple_tag(takes_context=True)
def sodaseo_render_value(context, value):
    t = Template(value)
    c = Context(context)
    return t.render(c)


@register.simple_tag
def sodaseo_render_og_see_also(value):
    template_str = '''{% for link in links %}
        <meta property="og:see_also" content="{{ link }}" />
    {% endfor %}'''
    t = Template(template_str)
    c = Context({'links': value.splitlines()})
    return t.render(c)
