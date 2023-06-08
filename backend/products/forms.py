from django import forms 
from .models import Product

class ProductForm(forms.ModelForm):
    class META:
        model=Product
        fields=[
            'title',
            'content',
            'price'
        ]