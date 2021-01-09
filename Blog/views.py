from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from.models import BlogPost, BlogPostComment

def blog(request):
    Blogs = BlogPost.objects.all()
    context = {}
    context['Blogs'] = Blogs
    return render(request, 'blog.html', context)

def blogdetails(request,blog_id):
    Blog = BlogPost.objects.get(id=blog_id)
    context = {}
    context['Blog'] = Blog
    return render(request, 'blogdetails.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = UserCreationForm()
    
    context = {}
    context['form'] = form
    return render(request, 'signup.html', context)