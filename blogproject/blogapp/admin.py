from django.contrib import admin
from blogapp.models import BlogModel

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogModel, BlogAdmin )

