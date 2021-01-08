from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

from.models import BlogPost, BlogPostComment

def blog(request):
    Blogs = BlogPost.objects.all()
    context = {}
    context['Blogs'] = Blogs
    return render(request, 'blog.html', context)
