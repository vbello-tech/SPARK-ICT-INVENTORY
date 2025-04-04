from django import forms
from .models import *
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from phonenumber_field.formfields import PhoneNumberField


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
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


category_list = ProductCategory.objects.all().values_list('name', 'name')
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

    detail = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'Detail, e.g, broken screen, rough back-case e.t.c',
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


class CheckOutForm(forms.Form):
    buyer = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "INPUT BUYER'S NAME",
    }))
    phone = PhoneNumberField(region="CA", widget=RegionalPhoneNumberWidget(attrs={
        'class': 'form-control',
        'placeholder': "INPUT BUYER'S PHONE NUMBER",
    }))
