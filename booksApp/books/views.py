from django.shortcuts import render , get_object_or_404 ,redirect, reverse
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
           return render(request , './books/contact.html' )

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

def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    # return HttpResponse("Product deleted")
    url = reverse("products.index")
    return redirect(url)


def product_create(request):
    # print(request)
    if request.method == "POST":
        print(request.FILES)
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        print(request.POST)
        product = Product(title=request.POST["title"], price=request.POST["price"],
                          code=request.POST["code"],author=request.POST["author"],
                          no_of_pages=request.POST["no_of_pages"], image=image)
        product.save()
        return redirect(product.show_url)
        # return HttpResponse("Post request received")
    # post request

    # get request
    return  render(request, 'books/crud/create.html')




def product_update(request,id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = product.image
        product.title = request.POST["title"]
        product.author = request.POST["author"]
        product.price = request.POST["price"]
        product.no_of_pages = request.POST["no_of_pages"]
        product.image = image
        product.save()
        # url = reverse("products.index")

        return redirect(product.show_url)

    return render(request, "books/crud/update.html", context={"product":product})