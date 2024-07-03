from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'tittle' : 'login',
    }
    
    return render(request, 'main/login.html', context)

def registration(request):
    context = {
        'tittle' : 'registration'
    }
    
    return render(request, 'main/registration.html')