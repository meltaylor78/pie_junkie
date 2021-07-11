from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('int:<product_id>/', views.details, name='details'),
    path('new/', views.new_product, name='new_product'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),
]
