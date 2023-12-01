from django.urls import path, re_path

from .views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    re_path('posts/(?P<slug>[-\w]+)/', PostDetailView.as_view(), name='post_detail'),
]