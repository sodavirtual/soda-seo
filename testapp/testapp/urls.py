# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings


admin.autodiscover()


urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),

    url(r'^posts/$', 'posts.views.post_list', name='post_list'),
    url(
        r'^posts/(?P<pk>[0-9]+)/$', 'posts.views.post_detail',
        name='post_detail'
    ),
)


if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True
            }
        ),
    )
