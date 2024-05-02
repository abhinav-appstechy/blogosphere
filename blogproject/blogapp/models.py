from django.db import models

# Create your models here.

class BlogModel(models.Model):

    blog_title = models.CharField(max_length=100)
    blog_desc = models.TextField()
    blog_category = models.CharField(max_length=50)
    blog_image = models.FileField(upload_to="blog_images/", blank=True)
    blog_views_count = models.IntegerField(max_length=20, default=0)
    blog_likes_count = models.IntegerField(max_length=20, default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.blog_title
    

