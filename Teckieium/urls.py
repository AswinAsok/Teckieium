"""Teckieium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Blog.views import blog,signup,blogdetails,authordetails,bloggers,createcomment,bio,createblog,profile,deleteblog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',blog,name='blog'),
    path('',blog,name='blog'),
    path('accounts/signup/',signup, name='signup'),
    path('accounts/signup/bio',bio, name='bio'),
    path('profile/',profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/bloggers/', bloggers, name='bloggers'),
    path('blog/create/', createblog, name='createblog'),
    path('blog/delete/<blog_id>', deleteblog, name='deleteblog'),
    path('blog/<blog_id>/create/', createcomment, name='createcomment'),
    path('blog/<blog_id>/', blogdetails, name='blogdetails'),
    path('blog/blogger/<author_id>', authordetails, name='authordetails')
   
]
