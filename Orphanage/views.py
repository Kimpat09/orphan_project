from django.shortcuts import render
from .models import Children
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
    childrenlist   = Children.objects.all()
    context        = {
        'childrenlist': childrenlist,
    }
    return render(request, 'pages/Childrenlist.html', context)


