from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Home/index.html')

def login(request):
    return render(request, 'Home/login.html')

def register(request):
    return render(request, 'Home/register.html')