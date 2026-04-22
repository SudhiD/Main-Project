from django import forms
from shope.models import Category, Products

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description', 'image']

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'image', 'description', 'caterory', 'stock']

class StockForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['stock']        