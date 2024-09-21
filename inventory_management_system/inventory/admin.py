from django.contrib import admin

# Register your models here.
from .models import Category, Location, Customer, Product, SalesFact

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(SalesFact)