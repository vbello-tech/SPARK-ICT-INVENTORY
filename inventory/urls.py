from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('search-func/', search_func, name='search_func'),
    path('add-category/', add_category, name="add_category"),
    path('add-product/', AddProduct.as_view(), name="add_product"),
    path('sold/<int:pk>/', sold, name="sold"),
    path('list/', ProductsView.as_view(), name="products"),
    path('detail/<int:pk>/', productdetail, name="product_detail"),
    path('categories/', CategoryView.as_view(), name="categories"),
    path('inventory-history/', history, name="history"),
    path('search/', Search.as_view(), name="search"),
    path('checkout/<int:pk>/', CheckoutView.as_view(), name="checkout"),
]
