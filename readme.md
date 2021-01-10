<div align="center">

<img height=20% width=20% src = "https://github.com/AswinAsok/Teckieium/blob/master/Teckieium%20Images/Logo.png">

</div>


# More Details About the Project 👇
<hr>

## Urls 🔗
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

## Pages 📄

#### <ins>Home Page
```
path('blog/',blog,name='blog')

path('',blog,name='blog')
```

<div align="center">
<img width=80% height=80% src="https://github.com/AswinAsok/Teckieium/blob/master/Teckieium%20Images/Home%20page.png">
</div>

#### <ins>Authorization Pages

```
path('accounts/signup/',signup, name='signup')

path('accounts/signup/bio',bio, name='bio')

path('accounts/', include('django.contrib.auth.urls'))

```

<div align="center">
<img width=80% height=80% src="https://github.com/AswinAsok/Teckieium/blob/master/Teckieium%20Images/Signup%20page.png">
<img width=80% height=80% src="https://github.com/AswinAsok/Teckieium/blob/master/Teckieium%20Images/Enter%20Bio.png">
<img width=80% height=80% src="https://github.com/AswinAsok/Teckieium/blob/master/Teckieium%20Images/Author%20details.png">
<img width=80% height=80% src="https://github.com/AswinAsok/Teckieium/blob/master/Teckieium%20Images/Login.png">
</div>


#### <ins>Blog Related Page

```
path('blog/bloggers/', bloggers, name='bloggers')

path('blog/<blog_id>/create/', createcomment, name='createcomment')

path('blog/<blog_id>/', blogdetails, name='blogdetails')

path('blog/blogger/<author_id>', authordetails, name='authordetails')
```
<div align="center">
<img width=80% height=80% src = "https://github.com/AswinAsok/Teckieium/blob/master/Teckieium%20Images/Bloggers.png">
<img width=80% height=80% src = "https://github.com/AswinAsok/Teckieium/blob/master/Teckieium%20Images/comment%20creation.png">
<img width=80% height=80% src = "https://github.com/AswinAsok/Teckieium/blob/master/Teckieium%20Images/Blog%20details%20page.png">
<img width=80% height=80% src = "https://github.com/AswinAsok/Teckieium/blob/master/Teckieium%20Images/login%20alert%20for%20commenting.png">
</div>
