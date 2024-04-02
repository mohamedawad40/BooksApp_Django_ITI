from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.


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
    "image": "to_kill_a_mockingbird.jpg"
  },
  {
    "id":2,
    "title": "1984",
    "no_of_pages": 328,
    "author": "George Orwell",
    "price": 9.49,
    "image": "1984.jpg"
  },
  {
    "id":3,
    "title": "The Great Gatsby",
    "no_of_pages": 180,
    "author": "F. Scott Fitzgerald",
    "price": 7.99,
    "image": "the_great_gatsby.jpg"
  },
  {
    "id":4,
    "title": "Pride and Prejudice",
    "no_of_pages": 279,
    "author": "Jane Austen",
    "price": 8.79,
    "image": "pride_and_prejudice.jpg"
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