from books.views import (hello , welcome , booklist ,book_details,
                         books_home,book_profile , contact,info,
                         products_index,product_show , product_delete,
                         product_create ,product_update)
from django.urls import path

urlpatterns = [
    path("booklist", booklist, name= "booklist"),
    path('prd/<int:id>',  book_details, name="product_detail"),
    path('home',  books_home, name='books-home'),
    path('contact',  contact, name='contact'),
    path('info',  info, name='info'),
    path('old/<int:id>', book_profile , name='book_profile'),
    path('', products_index, name='products.index'),
    path('<int:id>', product_show, name='products.show'),
    path('<int:id>/delete', product_delete, name='products.delete'),
    path('create', product_create, name='products.create'),
    path('update/<int:id>', product_update, name='products.update'),
]
   