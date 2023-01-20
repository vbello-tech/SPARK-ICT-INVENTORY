from django import forms
from .models import *

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Product_Category
        fields = ('name', 'quantity')

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'NAME OF THE CATEGORIES',
                }
            ),
            'quantity': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'QUANTITY OF THE CATEGORIES',
                }
            ),
        }

category_list = Product_Category.objects.all().values_list('name', 'name')
product_cat_choice = []
for item in category_list:
    product_cat_choice.append(item)

class AddProductForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'NAME OF THE PHONE',
    }))

    color = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'COLOR OF THE PHONE',
    }))

    dent = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'DENT, e.g, broken screen, rough back-case e.t.c',
    }))

    imei = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        "placeholder": 'IMEI NUMBER OF THE PHONE',
    }))

    spec = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'RAM AND ROM OF THE PHONE',
    }))

    type = forms.ChoiceField(required=False,
        choices=product_cat_choice,
         widget=forms.Select(attrs={
             'class': 'form-control bootstrap-select',
    }))

