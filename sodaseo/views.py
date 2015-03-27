# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.contenttypes.models import ContentType

from sodaseo.models import Seo


class SodaSeoMixin(object):

    def get_context_data(self, **kwargs):
        context = super(SodaSeoMixin, self).get_context_data(**kwargs)

        try:
            context['sodaseo'] = Seo.objects.get(
                content_type=ContentType.objects.get_for_model(self.object),
                object_id=self.object.pk
            ).to_dict()
        except:
            pass

        return context
