from django.contrib import admin
from django.urls import path, include
from LLM_web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('', views.index, name='index')
]
