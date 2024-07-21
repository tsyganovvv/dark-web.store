from django.shortcuts import render

from products.models import Product, ProductCategory


# Create your views here.

def index(request):
    context={
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()}
    return render(request, 'products/index.html', context)
def product(request, id):
    context={
        'id' : request.path.split('/')[-1],
    }
    context['product'] = Product.objects.filter(id=context['id'])
    return render(request, 'products/product.html', context)