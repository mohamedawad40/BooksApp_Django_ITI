from django.urls import path
from categories.views import (home ,create_category,categories_index,
                              category_show,category_delete,edit_category)

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('home' ,home , name='categories.home'),
    path('create' ,create_category, name='categories.create'),
    path('' , login_required(categories_index), name='categories.index'),
    path('<int:id>' , login_required(category_show), name='categories.show'),
    path('<int:id>/delete', login_required(category_delete), name='categories.delete'),
    path('<int:id>/edit',login_required(edit_category),name='categories.edit')
]
