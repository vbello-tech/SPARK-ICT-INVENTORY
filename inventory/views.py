from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import TemplateView, DetailView, View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    products = Product.objects.filter(sold=False)[:8]
    context = {
        'products': products,
        'items': products.count(),
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def get_result(search_info, search_type):
    if search_type == "Product":
        return Product.objects.filter(
            name=search_info
        )
    elif search_type == "Category":
        return ProductCategory.objects.get(
            name=search_info
        )


@login_required(login_url='login')
def search_func(request):
    search_info = request.POST['search_info']
    search_type = request.POST['search_type']
    result = get_result(search_info, search_type)
    context = {
        'result': result,
        'search_type': search_type,
        'info': search_info,
    }
    return render(request, 'search_result.html', context)


class Search(TemplateView, LoginRequiredMixin):
    template_name = "search.html"


@login_required(login_url='login')
def add_category(request):
    form = AddCategoryForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddCategoryForm()
    context = {
        'form': form
    }
    return render(request, 'add_category.html', context)


class AddProduct(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        form = AddProductForm()
        context = {
            'form': form,
        }
        return render(self.request, 'add_product.html', context)

    def post(self, request, *args, **kwargs):
        form = AddProductForm(self.request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            color = form.cleaned_data.get('color')
            details = form.cleaned_data.get('detail')
            imei = form.cleaned_data.get('imei')
            spec = form.cleaned_data.get('spec')
            type = form.cleaned_data.get('type')
            print(name, color, details, imei, spec, type)

            new_product, created = Product.objects.get_or_create(
                name=name,
                color=color,
                details=details,
                imei=imei,
                spec=spec,
                type=type,
                checked_in=True,
                checked_in_date=timezone.now()
            )
            return redirect('/')
        else:
            return redirect('/')


@login_required(login_url='login')
def sold(request, pk):
    return redirect('checkout', pk=pk)


# CHECK OUT VIEW
class CheckoutView(View, LoginRequiredMixin):
    def get(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
            form = CheckOutForm()
            context = {
                'form': form,
                'product': product,
            }
        except ObjectDoesNotExist:
            return redirect("checkout")

        return render(self.request, 'check_out.html', context)

    def post(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
            form = CheckOutForm(self.request.POST or None)
            if form.is_valid():
                buyer = form.cleaned_data.get('buyer')
                phone = form.cleaned_data.get('phone')
                product.sold = True
                product.date_sold = timezone.now()
                product.seller = request.user
                product.buyer = buyer
                product.phone = phone
                product.save()
                product_category = ProductCategory.objects.get(name=product.type)
                product_category.quantity -= 1
                product_category.save()

                return redirect('/')
            else:
                return redirect('checkout')

        except ObjectDoesNotExist:
            return redirect('checkout')


class ProductsView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        product = Product.objects.all().order_by('-checked_in_date')
        context = {
            'product': product,
        }
        return render(self.request, 'product_list.html', context)


@login_required(login_url='login')
def productdetail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)


class CategoryView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        category = ProductCategory.objects.all()
        context = {
            'category': category,
        }
        return render(self.request, 'category_list.html', context)


@login_required(login_url='login')
def history(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'history.html', context)
