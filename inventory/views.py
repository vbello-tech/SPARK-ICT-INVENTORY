from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import TemplateView, DetailView, View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

# Create your views here.

def Home(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'home.html', context)

def Search(request):
    if request.method =="POST":
        search_info = request.POST['search_info']
        search_type = request.POST['search_type']
        print(search_info, search_type)
        if search_type == "Phone":
            product_result = Product.objects.filter(
                name = search_info
            )
            is_category = False
        if search_type == "Category":
            product_result= Product_Category.objects.get(
                name = search_info
            )
            is_category = True
        context = {
            'product_result': product_result,
            'is_category':is_category,
            'info':search_info,

        }
        return render(request, 'search.html', context)

def AddCategory(request):
    form = AddCategoryForm(request.POST)
    if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddCategoryForm()
    context = {
        'form':form
    }
    return render(request, 'add_category.html', context)


class AddPhone(View, LoginRequiredMixin):
    def get(self, request,  *args, **kwargs):
        form = AddProductForm()
        context = {
            'form': form,
        }
        return render (self.request, 'add_phone.html', context)

    def post(self, request, *args, **kwargs):
        form = AddProductForm(self.request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            color = form.cleaned_data.get('color')
            dent = form.cleaned_data.get('dent')
            imei = form.cleaned_data.get('imei')
            spec = form.cleaned_data.get('spec')
            type = form.cleaned_data.get('type')
            print(name, color, dent, imei, spec, type)

            new_product, created = Product.objects.get_or_create(
                name = name,
                color = color,
                dent = dent,
                imei = imei,
                spec = spec,
                type = type,
                checked_in = True,
                checked_in_date = timezone.now()
            )
            return redirect('/')
        else:
            return redirect('/')

def sold(request, pk):
    product = Product.objects.get(pk=pk)
    product.sold = True
    product.date_sold = timezone.now()
    product.seller = request.user
    product.save()
    product_category = Product_Category.objects.get(name=product.type)
    product_category.quantity -= 1
    product_category.save()
    print(product_category)
    return redirect('/')

class ProductsView(View, LoginRequiredMixin):
    def get(self, request,  *args, **kwargs):
        product = Product.objects.all()
        context = {
            'product': product,
        }
        return render (self.request, 'product_list.html', context)

class CategoryView(View, LoginRequiredMixin):
    def get(self, request,  *args, **kwargs):
        category = Product_Category.objects.all()
        context = {
            'category': category,
        }
        return render (self.request, 'category_list.html', context)

def History(request):
    product = Product.objects.all()
    context = {
        'product':product
    }
    return render(request, 'history.html', context)
