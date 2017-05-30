from django.contrib import admin

from sodaseo.admin import SeoInline
from posts.models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title', 'created_at', 'updated_at'
    )
    inlines = [SeoInline, ]


admin.site.register(Post, PostAdmin)
