from django.forms import ModelForm
from .models import BlogPostComment


class CommentForm(ModelForm):

    class Meta:
        model = BlogPostComment
        fields = ('blog' , 'comment')