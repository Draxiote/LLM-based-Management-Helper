from django.contrib import admin
from django.urls import path, include
from LLM_web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    # path('', views.index, name='index'),
    
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('teachers', views.teachers, name='teachers'),
    path('update', views.update, name='update'),
]
