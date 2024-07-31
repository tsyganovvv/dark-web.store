from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from products.models import Product, ProductCategory, Order
from products.forms import createOrder
from django.http import QueryDict

# Create your views here.

def index(request):
    context={
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()}
    return render(request, 'products/index.html', context)

def product(request, id):
    product_ = Product.objects.get(id=id)
    if request.method == 'POST':
        form = createOrder(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_name = request.user
            post.num = request.POST['rangeInput']
            post.product_name = product_.name
            try:
                post.save()
            except Exception:
                person = Order.objects.get(user_name=request.user.username)
                person.delete()
                post.save()
            return HttpResponseRedirect(reverse('main:products:order', kwargs={'id':id}))
    else:
        form = createOrder()
    context={
        'id' : request.path.split('/')[-1],
        'form' : form,
    }
    context['product'] = product_

    return render(request, 'products/product.html', context)
def order(request, id):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('main:products:success'))
    context = {
        
        'id' : request.path.split('/')[-2],
    }
    context['product'] = Product.objects.get(id=context['id'])
    context['order'] = Order.objects.get(user_name=request.user)
    
    return render(request, 'products/order.html', context)

def success(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('main:products:index'))
    return render(request, 'products/success.html')
