from django.shortcuts import render , get_object_or_404 ,redirect, reverse
from django.http import HttpResponse
from books.forms import BookForm ,ProductModelForm
from categories.models import Category
from django.views import generic
from django.db.models import Q
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
    latest_books = Product.objects.order_by('-created_at')[:4]
    return render(request , 'books/crud/index.html' ,
                  context={"products" : products,"latest_books":latest_books})

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


def product_create_forms(request):
    form=BookForm()
    category = get_object_or_404(Category, pk=1)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            product = Product(title=form.cleaned_data["title"], price=form.cleaned_data["price"],
                          code=form.cleaned_data["code"],author=form.cleaned_data["author"],
                          no_of_pages=form.cleaned_data["no_of_pages"], image=form.cleaned_data['image'],
                              category=category)
            product.save()
            return redirect(product.show_url)

    return render(request,'books/forms/create.html',
                  context={'form':form})

def product_create_model_forms(request):
    form = ProductModelForm()
    if request.method == "POST":
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(product.show_url)

    return  render(request , 'books/forms/createmodelform.html',
                   context={'form' :form})


def edit_product(request, id):
    product= Product.get_product_by_id(id)
    form = ProductModelForm(instance=product)
    if request.method == "POST":
        form = ProductModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect(product.show_url)


    return render(request, 'books/forms/edit.html',
              context={"form": form})



class BookSearchView(generic.ListView):
    template_name = 'books/crud/index.html'
    model = Product
    context_object_name = 'books'

    def get_queryset(self):
        search_query = self.request.GET.get('search_query')
        books = Product.objects.filter(
            Q(title__icontains=search_query) | Q(author__icontains=search_query)
        )
        print(books)
        self.extra_context = {'search_query': search_query}
        return books