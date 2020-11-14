from .models import Products
from django import forms 
from django.contrib.auth.models import User

class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields=['name','price']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'})
        }

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','password']
        help_texts={
            'username':None
        }
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'})
        }