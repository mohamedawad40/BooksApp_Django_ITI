from django import forms
from categories.models import Category



class CategoryModelForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

    def clean_name(self):
            name = self.cleaned_data.get('name')
            if name is None or len(name) < 3:
                raise forms.ValidationError('Name must be provided and have a length greater than 3 characters')
            return name


