from django.urls import path

from main.views import login, registration, index, logout, about, contact


app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('registration', registration, name='registration'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]
