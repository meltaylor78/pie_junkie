from django.contrib import admin
from .models import Product, Category, Cust_Review


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

class ReviewsAdmin(admin.ModelAdmin):
    list_display =(
        'date',
        'user',
        'product',
        'title',
        'recommend'
    )

    ordering = ('-date',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cust_Review, ReviewsAdmin)
