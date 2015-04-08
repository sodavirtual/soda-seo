# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from django.contrib.sites.models import Site
from django.template import Context, Template
from django.contrib.contenttypes.models import ContentType

from sodaseo.models import Config, Url, Seo, get_default_template
from sodaseo.utils import convert_url


register = template.Library()


@register.simple_tag(takes_context=True)
def sodaseo_render_tags(context, site_id=1):
    request = context['request']

    # load site
    try:
        site = Site.objects.get(pk=site_id)
    except Site.DoesNotExist:
        return ''

    # load config
    try:
        config = Config.objects.get(site=site)
        config_sodaseo = Seo.objects.get(
            content_type=ContentType.objects.get_for_model(Config),
            object_id=config.pk
        ).to_dict()
        config_sodaseo.update(config.to_dict())
    except:
        config = None
        config_sodaseo = {}

    # load url
    try:
        url = Url.objects.get(
            site=site,
            path=convert_url(request.get_full_path())
        )
        url_sodaseo = Seo.objects.get(
            content_type=ContentType.objects.get_for_model(Url),
            object_id=url.pk
        ).to_dict()
    except:
        url = None
        url_sodaseo = {}

    # load sodaseo from context
    sodaseo_ctx = context.get('sodaseo', {})

    # template
    template = ''

    if config_sodaseo:
        template = config_sodaseo['template'].body

    if url_sodaseo:
        template = url_sodaseo['template'].body

    if sodaseo_ctx:
        template = sodaseo_ctx['template'].body

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
