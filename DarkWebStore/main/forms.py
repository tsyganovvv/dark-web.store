from django import forms
from django.contrib.auth.forms  import AuthenticationForm, UserCreationForm
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

class UserCreateForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class' : 'label',
        'place_holder' : 'Эл. почта',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'label',
        'place_holder' : 'Имя пользователя',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'label',
        'place_holder' : 'Пароль',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'label',
        'place_holder' : 'Подтвердите пароль',
    }))
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2',)
