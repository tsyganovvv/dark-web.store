from django import forms
from django.contrib.auth.forms  import AuthenticationForm
from main.models import User
from django.contrib.auth.models import AbstractUser

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'label',
        'place_holder' : 'Введите имя пользователя',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'label',
        'place_holder' : 'Введите пароль',
    }))
    class Meta:
        model = AbstractUser
        fields = ('username', 'password',)