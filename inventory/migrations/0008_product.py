# Generated by Django 4.1.5 on 2023-01-12 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0007_rename_phone_category_product_category_delete_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('color', models.CharField(max_length=300)),
                ('type', models.CharField(blank=True, choices=[('samsung s10', 'samsung s10'), ('iphone 6', 'iphone 6'), ('apple watch', 'apple watch')], max_length=300, null=True)),
                ('imei', models.IntegerField(blank=True, null=True)),
                ('sold', models.BooleanField(default=False)),
                ('checked_in', models.BooleanField(default=False)),
                ('spec', models.CharField(max_length=300)),
                ('dent', models.CharField(blank=True, max_length=300, null=True)),
                ('date_sold', models.DateField(blank=True, null=True)),
                ('checked_in_date', models.DateField(blank=True, null=True)),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]