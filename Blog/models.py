from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    blog_title = models.CharField(max_length = 30, blank=False)
    blog_author = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    blog_content = models.TextField(max_length=5000, blank=False,default="")
    blog_date = models.DateField(blank=True, null=True) 

    def __str__(self):
        return self.blog_title
    
    class Meta:
        ordering = ('-blog_date')


class BlogPostComment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE,default="")
    comment = models.CharField(max_length=20, blank=True)
    comment_date = models.DateField(blank=True, null=True) 
    comment_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.comment

   
