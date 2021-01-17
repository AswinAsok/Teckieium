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

class Updateblog(ModelForm):

    class Meta:
        model = BlogPost
        fields = fields = ('blog_title' ,'blog_author' ,'blog_content')
        
