from django.db import models
from django.urls import reverse

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models .CharField(max_length=128, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

class Order(models.Model):
    telegram = models.CharField(max_length=128)
    num = models.IntegerField(default=1)
    user_name = models.CharField(max_length=128, unique=True)
    product_name = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return f'Телеграм: {self.telegram} | Количество: {self.num}'
    