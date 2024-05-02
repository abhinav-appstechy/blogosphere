from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index),
    path('blog/<str:name>/', views.single_blog),
    path('about-us/', views.about_us, name="about_us"),
    path('contact-us/', views.contact_us, name="contact_us"),
    # Catch-all pattern to redirect to the homepage
    # path('<path:invalid_path>', RedirectView.as_view(url='/')),
    
]