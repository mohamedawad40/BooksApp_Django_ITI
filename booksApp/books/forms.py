from django import forms
from books.models import Product
class BookForm(forms.Form):
    title = forms.CharField(max_length=100,
                          label='Product Title', required=True)
    author = forms.CharField(max_length=100,
                             label='Product Author', required=True)
    no_of_pages = forms.IntegerField(label='no_of_pages', required=True)
    price = forms.IntegerField(label='Price', required=True)
    image = forms.ImageField(required=False, label='Image')
    code = forms.CharField(max_length=100)

    ## unique validation
    ## check code --> not exists before in the database

    def clean_code(self):
        code = self.cleaned_data['code']
        ## code --> check if exits before in the database
        code_found = Product.objects.filter(code=code).exists()
        if code_found:
            raise forms.ValidationError('Code used before , please choose another one')

        return code

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError('Title length must be greater than 2 characters')
        return title

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price <= 0:
            raise forms.ValidationError('Price must be a positive number')
        return price



