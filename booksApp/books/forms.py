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
        if title is None or len(title) < 3:
            raise forms.ValidationError('Title must be provided and have a length greater than 3 characters')
        return title

    def clean_price(self):
        price = self.cleaned_data['price']
        if price is  None or price < 20:
            raise forms.ValidationError('Price should be greater than 20$')
        return price

    def clean_no_of_pages(self):
        pages = self.cleaned_data['no_of_pages']
        if pages is None :
            raise forms.ValidationError('Number of pages should be greater than 10')
        return pages

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if author is None or len(author) < 3:
            raise forms.ValidationError('Author must be provided and have a length greater than 3 characters')
        return author
