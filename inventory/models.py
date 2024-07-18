from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Product_Category(models.Model):
    name = models.CharField(max_length=300)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


category_list = Product_Category.objects.all().values_list('name', 'name')
product_cat_choice = []
for item in category_list:
    product_cat_choice.append(item)


class Product(models.Model):
    name = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    type = models.CharField(max_length=300, choices=product_cat_choice, blank=True, null=True)
    imei = models.IntegerField(blank=True, null=True)
    sold = models.BooleanField(default=False)
    checked_in = models.BooleanField(default=False)
    spec = models.CharField(max_length=300)
    details = models.CharField(max_length=300, blank=True, null=True)
    date_sold = models.DateField(blank=True, null=True)
    checked_in_date = models.DateField(blank=True, null=True)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    buyer = models.CharField(max_length=300, blank=True, null=True)
    buyer_phone = PhoneNumberField(blank=True, null=True)

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return self.name
