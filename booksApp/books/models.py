from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    no_of_pages = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    # image = models.ImageField(upload_to='products/images', null=True, blank=True)
    code = models.CharField(max_length=100 , unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)