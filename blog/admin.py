from django.contrib import admin

from .models import Post, Comment


class CommentsInline(admin.StackedInline):
    model = Comment
    fields = ['user', 'text', 'status', 'active',]
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'slug', 'active', 'status', 'created_at',]
    search_fields = ['title',]
    list_editable = ['status', 'active',]
    ordering = ['created_at',]
    inlines = [CommentsInline,]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'status', 'active', 'created_at',]
    search_fields = ['user', 'post',]
    list_editable = ['status', 'active',]
