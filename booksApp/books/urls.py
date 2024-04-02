from books.views import hello , welcome , booklist ,book_details
from django.urls import path

urlpatterns = [
    path("booklist" , booklist , name= "booklist"),
    path('prd/<int:id>' ,  book_details , name="product_detail")
]
