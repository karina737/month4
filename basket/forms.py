from django import forms
from basket.models import Basket

class BasketForms(forms.ModelForm):
    class Meta:
        model = Basket
        fields = '__all__'
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'input'}),
            'quantity': forms.NumberInput(attrs={'class': 'input'}),
            'status_delivery': forms.Select(attrs={'class': 'input'}),
        }

