from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import AbstractUser
from main.forms import UserLoginForm, UserCreateForm
from django.contrib import auth
from django.urls import reverse

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm
    
    context = {
        'form': form,
    }
    return render(request, 'main/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:login'))
    else:
        form = UserCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'main/registration.html', context)
def index(request):
    context = {}
    return render(request, 'main/index.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

def about(request):
    context = {}
    return render(request, 'main/about.html', context)

def contact(request):
    context = {}
    return render(request, 'main/contact.html', context)