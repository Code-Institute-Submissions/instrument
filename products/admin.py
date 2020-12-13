from django.contrib import admin
from .models import Product, Category

# Register your models here.

# This changes the display of the normal django default of the displayed attributes.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


# This displays the friendly name that we predefined to make it nicer to read.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product)
admin.site.register(Category)