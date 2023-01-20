from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name="home"),
    path('search/', Search, name='search'),
    path('add-category/', AddCategory, name="add_category"),
    path('add-phone/', AddPhone.as_view(), name="add_phone"),
    path('sold/<int:pk>/', sold, name="sold"),
    path('products/', ProductsView.as_view(), name="products"),
    path('categories/', CategoryView.as_view(), name="categories"),
    path('inventory-history/', History, name="history"),
]