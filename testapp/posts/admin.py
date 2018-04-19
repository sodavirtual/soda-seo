from django.contrib import admin

from posts.models import Post
from sodaseo.admin import SeoInline


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'created_at', 'updated_at'
    )
    inlines = [SeoInline, ]


admin.site.register(Post, PostAdmin)
