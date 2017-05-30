from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from sodaseo.views import SodaSeoMixin
from posts.models import Post


class PostListView(ListView):

    template_name = 'posts/list.html'

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(SodaSeoMixin, DetailView):

    template_name = 'posts/detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Post, pk=pk)
