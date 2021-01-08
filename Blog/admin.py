from django.contrib import admin
from .models import BlogPost, BlogPostComment

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('blog_title','blog_author', 'blog_date')

    search_fields = ('blog_title', 'blog_author')

    class Meta:
        model = BlogPost

class BlogPostCommentAdmin(admin.ModelAdmin):
    list_display = ('comment','comment_date','comment_time')

    class Meta:
        model = BlogPostComment

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(BlogPostComment,BlogPostCommentAdmin)