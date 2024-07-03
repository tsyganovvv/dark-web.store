from django.urls import path

from main.views import login, registration


app_name = 'products'

urlpatterns = [
    path('', login, name='login'),
    path('registration', registration, name='registration')
]
