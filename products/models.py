from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    power = models.BooleanField(max_length=254, null=True, blank=True)
    ram = models.BooleanField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Cust_Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, blank=True)
    recommend = models.CharField(max_length=10, blank=True)
    review = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return self.review

