from django.shortcuts import render

from products.models import Product, ProductCategory


# Create your views here.

def index(request):
    context={
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()}
    return render(request, 'products/index.html', context)