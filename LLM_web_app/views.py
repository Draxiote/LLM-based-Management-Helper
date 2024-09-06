from django.shortcuts import render, HttpResponse   

# Create your views here.

def index(request):
    
    return render(request, 'index.html')
    
    # return HttpResponse('This is Home page')
    
    

def about(request):
    return render(request, 'main_screen/about.html')
    
def contact(request):
    return render(request, 'main_screen/contact.html')

def courses(request):
    return render(request, 'main_screen/courses.html')

def home(request):
    return render(request, 'main_screen/home.html')

def profile(request):
    return render(request, 'main_screen/profile.html')

def teachers(request):
    return render(request, 'main_screen/teachers.html')

def update(request):
    return render(request, 'main_screen/update.html')
