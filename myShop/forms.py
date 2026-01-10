from django import forms
from myShop.models import Category, Product

class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
   
class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'