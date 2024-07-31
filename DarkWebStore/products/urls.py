from django.urls import path

from products.views import index, product, order


app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>', product, name='product'),
    path('<int:id>/order', order, name='order'),
]
