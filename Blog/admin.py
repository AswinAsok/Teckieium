from django.contrib import admin
from .models import BlogPost

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('blog_title','blog_author', 'blog_date')
    search_fields = ('blog_title', 'blog_author')

    class Meta:
        model = BlogPost

admin.site.register(BlogPost,BlogPostAdmin)