from django.shortcuts import render
from django.views import generic

from .models import Post


class PostListView(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    ordering = 'title'
