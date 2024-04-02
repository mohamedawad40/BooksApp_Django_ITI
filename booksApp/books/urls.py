from books.views import (hello , welcome , booklist ,book_details,books_home,book_profile , contact,info)
from django.urls import path

urlpatterns = [
    path("booklist" , booklist , name= "booklist"),
    path('prd/<int:id>' ,  book_details , name="product_detail"),
    path('home' ,  books_home , name='books-home'),
    path('contact' ,  contact , name='contact'),
    path('info' ,  info , name='info'),

    path('<int:id>' , book_profile , name='book_profile'),
]
   