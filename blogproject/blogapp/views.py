from django.shortcuts import render
from blogapp.models import BlogModel
from django.shortcuts import get_object_or_404
from django.contrib.sessions.models import Session

# Create your views here.
def index(request):
    blogs = BlogModel.objects.all()
    num_blogs = len(blogs)
    
    context = {
        "blogs": blogs,
        "num_blogs": num_blogs,
        "activeLink": "Home"
    }
    print(context)

    return render(request, "homepage.html", context)


def single_blog(request,name):
    print(name)
    # blog = get_object_or_404(BlogModel, blog_title=name)
    blog = BlogModel.objects.filter(blog_title__contains=name).first()
    session_key = request.session.session_key
    if not request.session.get(f'blog_{blog.id}_visited', False):
        # Increment the view count only if the user hasn't visited this page before
        blog.blog_views_count += 1
        blog.save()
        
        # Set a session flag indicating that the user has visited this page
        request.session[f'blog_{blog.id}_visited'] = True
    print(blog)
    context = {
        "blog": blog
    }
    return render(request, "single_blog_page.html", context)

def about_us(request):
    context = {
        "array": [1,1,1,1],
        "activeLink": "Our Team"
    }
    return render(request, "aboutus.html", context)

def contact_us(request):
    context = {
        "activeLink": "Contact Us"
    }

    return render(request, "contactus.html", context)

