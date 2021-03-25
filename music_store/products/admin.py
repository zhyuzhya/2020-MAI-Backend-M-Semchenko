from django.contrib import admin
from products.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'producer', 'year', 'color', 'current_price', 'category')
    pass

admin.site.register(Product, ProductAdmin)
