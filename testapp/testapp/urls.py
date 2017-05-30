from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.views.static import serve

from posts.views import PostListView, PostDetailView
from sodaseo.views import render_tags_detail

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^posts/$', PostListView.as_view(), name='post_list'),
    url(
        r'^posts/(?P<pk>[0-9]+)/$', PostDetailView.as_view(),
        name='post_detail'
    ),
    url(r'^sodaseo/$', render_tags_detail, name='render_tags_detail'),
]


if settings.DEBUG:
    urlpatterns += [
        url(
            r'^media/(?P<path>.*)$',
            serve,
            {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True
            }
        ),
    ]
