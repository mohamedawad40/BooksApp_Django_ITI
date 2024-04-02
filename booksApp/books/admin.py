from django.contrib import admin

# Register your models here.
from books.models import Product

admin.site.register(Product)