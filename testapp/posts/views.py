from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from posts.models import Post
from sodaseo.views import SodaSeoMixin


class PostListView(ListView):
    template_name = 'posts/list.html'

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(SodaSeoMixin, DetailView):
    template_name = 'posts/detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Post, pk=pk)
