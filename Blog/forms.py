from django.forms import ModelForm
from .models import BlogPost,BlogPostComment


class CommentForm(ModelForm):
    class Meta:
        model = BlogPostComment
        fields = ('blog' , 'comment')

    def __init__(self, blog_id, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = BlogPost.objects.filter(id = blog_id)