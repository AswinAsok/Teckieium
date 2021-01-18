from django.forms import ModelForm
from .models import BlogPost,BlogPostComment,Bio
from django.contrib.auth.models import User


class CommentForm(ModelForm):
    class Meta:
        model = BlogPostComment
        fields = ('blog' , 'comment')

    def __init__(self, blog_id, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = BlogPost.objects.filter(id = blog_id)

class BioForm(ModelForm):

    class Meta:
        model = Bio
        fields = ('user', 'bio')

    def __init__(self, user, *args, **kwargs):
        super(BioForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(username=user)

class CreateBlog(ModelForm):

    class Meta:
        model = BlogPost
        fields = ('blog_title' ,'blog_author' ,'blog_content')

    def __init__(self, user, *args, **kwargs):
        super(CreateBlog, self).__init__(*args, **kwargs)
        self.fields['blog_author'].queryset = User.objects.filter(username=user)

class UpdateBlog(ModelForm):

    class Meta:
        model = BlogPost
        fields = ('blog_title' ,'blog_author' ,'blog_content')

    def __init__(self,Blog, *args, **kwargs):
        super(UpdateBlog, self).__init__(*args, **kwargs)
        self.fields['blog_title'].disabled = True
        self.fields['blog_title'].initial = Blog.blog_title
        self.fields['blog_author'].disabled = True
        self.fields['blog_author'].initial = Blog.blog_author
        self.fields['blog_content'].initial = Blog.blog_content
        
    
        
