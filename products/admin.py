from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display =(
        'sku',
        'name',
        'category',
        'image',
        'power',
        'ram',
    )

    ordering = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display =(
        'friendly_name',
        'name'
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
