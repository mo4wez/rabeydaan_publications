from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'slug', 'active', 'status', 'created_at']
    search_fields = ['title',]
    list_editable = ['status', 'active',]
    ordering = ['created_at',]