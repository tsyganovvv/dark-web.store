from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import AbstractUser
from main.forms import UserLoginForm
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
                return HttpResponseRedirect(reverse('main:registration'))
    else:
        form = UserLoginForm
    
    context = {
        'form': form,
    }
    return render(request, 'main/login.html', context=context)

def registration(request):
    context = {
        'tittle' : 'registration'
    }
    
    return render(request, 'main/registration.html')