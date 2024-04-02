from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
import json
# Create your views here.

from books.models import Product

def hello(request):
    print(request)
    return HttpResponse("we are here....")

def welcome(request):
    name='awad'
    return HttpResponse(f"welcome{name}")

Books=[
  {
    "id":1,
    "title": "To Kill a Mockingbird",
    "no_of_pages": 281,
    "author": "Harper Lee",
    "price": 10.99,
    "image": "Aerie.jpg"
  },
  {
    "id":2,
    "title": "1984",
    "no_of_pages": 328,
    "author": "George Orwell",
    "price": 9.49,
    "image": "catwomen.jpg"
  },
  {
    "id":3,
    "title": "The Great Gatsby",
    "no_of_pages": 180,
    "author": "F. Scott Fitzgerald",
    "price": 7.99,
    "image": "Forest.png"
  },
  {
    "id":4,
    "title": "Pride and Prejudice",
    "no_of_pages": 279,
    "author": "Jane Austen",
    "price": 8.79,
    "image": "Defiant.jpeg"
  }
]

def booklist(request):
    return HttpResponse(Books)

def book_details(request,id):
    #id=int(id)
    filtered_products=filter(lambda product : product['id'] == id , Books ) #object
    print(filtered_products)
    allproducts=list(filtered_products)
    print(allproducts)
    if len(allproducts)>0:
#        return HttpResponse(allproducts[0])
        return HttpResponse(json.dumps( allproducts[0]))
    
    else:
        return HttpResponse("No Book Found")
    
def books_home(request):
    return render(request, "books/home.html" ,
                  context= {'books':Books},
                   status=200)

    
def book_profile(request,id):
       filtered_products=filter(lambda product : product['id'] == id , Books ) #object
       allproducts=list(filtered_products)
       if allproducts:
           product=allproducts[0]
           return render(request , './books/details.html' , context={
               "product":product
           })
       
def contact(request):
           return render(request , './books/contact.html' ) \

def info(request):
           return render(request , './books/info.html' )


def products_index(request):
    products=Product.objects.all()
    return render(request , 'books/crud/index.html' ,
                  context={"products" : products})

def product_show(request,id):
    # product=Product.objects.get(id=id)
    product=get_object_or_404( Product ,  pk=id)
    return render(request, 'books/crud/show.html',
                  context={"product": product})
