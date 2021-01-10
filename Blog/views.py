from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Bio,BlogPost
from .forms import CommentForm,BioForm,CreateBlog
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator,EmptyPage


# Create your views here.

from.models import BlogPost, BlogPostComment

def blog(request):
    Blogs = BlogPost.objects.all()
    p = Paginator(Blogs, 5)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    
    context = {}
    context['Blogs'] = page
    return render(request, 'blog.html', context)

def blogdetails(request,blog_id):
    Blog = BlogPost.objects.get(id=blog_id)
    comments = BlogPostComment.objects.filter(blog=BlogPost.objects.get(id=blog_id))
    context = {}
    context['Blog'] = Blog
    context['Comments'] = comments
    return render(request, 'blogdetails.html', context)

def authordetails(request, author_id):
    Author = User.objects.get(id=author_id)
    bio = Bio.objects.get(user = Author)
    blogs = BlogPost.objects.filter(blog_author = Author)
    context = {}
    context['Author'] = Author
    context['Bio'] = bio
    context['Blogs'] = blogs
    return render(request, "authordetails.html", context)

def bloggers(request):
    Bloggers = User.objects.all()
    context = {}
    context['Bloggers'] = Bloggers
    return render(request, "bloggers.html", context)

def createcomment(request,blog_id):
    if request.method == 'POST':
        form = CommentForm(blog_id,request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = CommentForm(blog_id)

    context = {}
    context['form'] = form
    context['blog_id'] = blog_id
    return render(request,"createcomment.html",context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('bio')
    else:
        form = UserCreationForm()
    
    context = {}
    context['form'] = form
    return render(request, 'signup.html', context)

def bio(request):

    if request.method == 'POST':
        form = BioForm(request.user.username,request.POST,)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BioForm(request.user.username)

    context = {}
    context['form'] = form
    return render(request,'bio.html', context)

def createblog(request):

    if request.method == 'POST':
        form = CreateBlog(request.user.username,request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = CreateBlog(request.user.username)
    
    context = {}
    context['form'] = form
    return render(request,'createblog.html', context)
        