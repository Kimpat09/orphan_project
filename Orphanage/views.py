from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def About(request):
    return render(request, 'pages/About.html')

def Gallery(request):
    return render(request, 'pages/Gallery.html')

def Login(request):
    return render(request, 'pages/Login.html')

def Dashboard(request):
    return render(request, 'pages/Dashboard.html')

def Childrenlist(request):
    return render(request, 'pages/Childrenlist.html')

