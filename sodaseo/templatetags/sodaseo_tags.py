# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from django.template import Context, Template

from sodaseo.models import Config, get_default_template, get_sodaseo_context


register = template.Library()


@register.simple_tag(takes_context=True)
def sodaseo_render_tags(context, site_id=1):
    sodaseo_ctx = context.get('sodaseo', {})
    request = context['request']
    ctx = get_sodaseo_context(request, sodaseo_ctx, site_id=site_id)

    # template
    template = get_default_template()

    try:
        template = ctx['template'].body
    except KeyError:
        pass

    try:
        t = Template(template)
        context.update({'sodaseo': ctx})
        c = Context(context)
        return t.render(c)
    except:
        pass

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


@register.inclusion_tag('sodaseo/analytics.html')
def sodaseo_render_analytics():
    google_analytics_id = ''

    try:
        config = Config.objects.all()[0]
        google_analytics_id = config.google_analytics_id
    except:
        pass

    return {
        'google_analytics_id': google_analytics_id
    }


@register.inclusion_tag('sodaseo/extra_head.html')
def sodaseo_render_extra_head():
    extra_head = None

    try:
        config = Config.objects.all()[0]
        extra_head = config.extra_head
    except:
        pass

    return {
        'extra_head': extra_head
    }


@register.inclusion_tag('sodaseo/extra_body.html')
def sodaseo_render_extra_body():
    extra_body = None

    try:
        config = Config.objects.all()[0]
        extra_body = config.extra_body
    except:
        pass

    return {
        'extra_body': extra_body
    }
