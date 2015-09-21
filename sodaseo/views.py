# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.contenttypes.models import ContentType
from django.views.generic import View
from django.http import HttpResponse
from django.template import Context, Template
from django.test import RequestFactory

from sodaseo.models import Seo


class SodaSeoMixin(object):

    def get_sodaseo_object(self):
        if getattr(self, 'object', None):
            try:
                return Seo.objects.get(
                    content_type=ContentType.objects.get_for_model(
                        self.object
                    ),
                    object_id=self.object.pk
                ).to_dict()
            except:
                pass

        return {}

    def get_context_data(self, **kwargs):
        context = super(SodaSeoMixin, self).get_context_data(**kwargs)
        context['sodaseo'] = self.get_sodaseo_object()
        return context


class RenderTagsDetail(View):

    def get(self, request):
        factory = RequestFactory()
        request = factory.get(request.GET.get('url', '/'))

        template_content = '''
        {% load sodaseo_tags %}
        <html>
        <head>
        {% sodaseo_render_tags site_id=1 %}
        </head>
        <body></body>
        </html>
        '''

        t = Template(template_content)
        c = Context({'request': request})
        return HttpResponse(t.render(c))


# cbv -> fbv
render_tags_detail = RenderTagsDetail.as_view()
