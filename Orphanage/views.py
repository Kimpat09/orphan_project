from django.shortcuts import render, redirect
from .models import Children, StatusForChildren
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserSignUpForm

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def About(request):
    return render(request, 'pages/About.html')

def Gallery(request):
    return render(request, 'pages/Gallery.html')

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('Childrenlist')

            return redirect('index')
        
    return render(request, 'pages/Login.html')

def registration (request):
    form = UserSignUpForm()
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')

            user = User.objects.create_user(
                username=username, first_name=first_name,
                last_name=last_name, password=password, email=email)
            
            login(request, user)
            return redirect('index')
    return render(request, 'pages/registration.html')

def sign_out(request):
    logout(request)
    return redirect('Login')

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
