from django import forms
from products.models import Order

class createOrder(forms.ModelForm):
    rangeInput = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type':'range',
        'step': '1',
        'class' : 'form-control',
        'min': '1',
        'max': '20',
        }), required=True,)
    telegram = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'place_holder' : 'Ваш Telegram',
    }), required=True,)
    class Meta:
        model = Order
        fields = ('telegram', 'rangeInput',)
    