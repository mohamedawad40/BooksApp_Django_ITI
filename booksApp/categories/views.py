from django.shortcuts import render , reverse, redirect,get_object_or_404
from categories.forms import CategoryModelForm
from categories.models import Category
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request,'template/categories/home.html')

@login_required
def create_category(request):
    print(request.user)
    form = CategoryModelForm()
    if request.method == "POST":
        form = CategoryModelForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            url =  reverse("categories.index")
            return  redirect(url)



    return render(request, 'categories/create.html',
                  {'form': form})




def categories_index(request):
    categories = Category.get_all_categories()
    return render(request, 'categories/index.html', {'categories' : categories})


def category_show(request, id):
    category = Category.get_category_by_id(id)
    return render(request, 'categories/show.html', {'category' : category})

def category_delete(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    # return HttpResponse("Product deleted")
    url = reverse("categories.index")
    return redirect(url)


def edit_category(request, id):
    product= Category.get_category_by_id(id)
    form = CategoryModelForm(instance=product)
    if request.method == "POST":
        form = CategoryModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect(product.show_url)


    return render(request, 'categories/edit.html',
              context={"form": form})