from django.db import models
from django.shortcuts import  reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(null=True,max_length=100, blank=True)
    no_of_pages = models.CharField(null=True,max_length=100, blank=True)
    author = models.CharField(null=True,max_length=100, blank=True)
    price = models.IntegerField(null=True, blank=True)
    # image = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='books/images', null=True, blank=True)
    code = models.CharField(max_length=100 , unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.title}'

    @property
    def show_url(self):
        pass
        url = reverse('products.show', args=[self.id])
        return url

    @property
    def delete_url(self):
        pass
        url = reverse('products.delete', args=[self.id])
        return url

    @property
    def image_url(self):
        return f"/media/{self.image}"

    @property
    def update_url(self):
        return reverse('products.update', args=[self.id])