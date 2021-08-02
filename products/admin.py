from django.contrib import admin
from .models import Product, Category, Customer_Review


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

class ReviewAdmin(admin.ModelAdmin):
    list_display =(
        'user',
        'product',
        'title',
        'recommend'
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer_Review, ReviewAdmin)
