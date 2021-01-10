<div align="center">

# <ins>Teckieium
----

</div>

## <ins>Urls
```
* path('admin/', admin.site.urls)

* path('blog/',blog,name='blog')

* path('',blog,name='blog')

* path('accounts/signup/',signup, name='signup')

* path('accounts/signup/bio',bio, name='bio')

* path('accounts/', include('django.contrib.auth.urls'))

* path('blog/bloggers/', bloggers, name='bloggers')

* path('blog/<blog_id>/create/', createcomment, name='createcomment')

* path('blog/<blog_id>/', blogdetails, name='blogdetails')

* path('blog/blogger/<author_id>', authordetails, name='authordetails')
```
-----

## <ins>Pages

#### <ins>Home Page
```
path('blog/',blog,name='blog')

path('',blog,name='blog')
```

<div align="center">
<img width=50% height=50% src="https://github.com/AswinAsok/Teckieium/blob/master/Teckieium%20Images/Home%20page.png">
</div>

#### <ins>Authorization Pages

```
path('accounts/signup/',signup, name='signup')

path('accounts/signup/bio',bio, name='bio')

path('accounts/', include('django.contrib.auth.urls'))

```

<img src = "">
<img src = "">
<img src = "">


#### <ins>Blog Related Page

```
path('blog/bloggers/', bloggers, name='bloggers')

path('blog/<blog_id>/create/', createcomment, name='createcomment')

path('blog/<blog_id>/', blogdetails, name='blogdetails')

path('blog/blogger/<author_id>', authordetails, name='authordetails')
```

<img src = "">
<img src = "">
<img src = "">
