from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog-detail.html'
    context_object_name = 'blog'