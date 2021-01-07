from django.db import models

# Create your models here.

class BlogPost(models.Model):
    blog_title = models.CharField(max_length = 30, blank=False)
    post_date = models.DateTimeField(blank=False),
    blog_content = models.CharField(blank=False),

    def __str__(self):
        return self.blog_title

