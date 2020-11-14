from .models import Products
from django import forms 

class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields=['name','price']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'})
        }