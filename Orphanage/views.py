from django.shortcuts import render
from .models import Children, StatusForChildren
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
    children  = StatusForChildren.objects.all()
    context        = {
        'children': children
    }
    return render(request, 'pages/Childrenlist.html', context)

def Viewchildren(request, pk):
    child = Children.objects.get(id=pk)
    context = {
        'child': child
    }
    return render(request, 'pages/Viewchildren.html', context)
