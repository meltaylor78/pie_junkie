from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('int:<product_id>/', views.details, name='details'),
    path('new/', views.new_product, name='new_product'),
    path('delete/<int:product_id>', views.delete_product,
         name='delete_product'),
    path('edit/<int:product_id>', views.edit_product,
         name='edit_product'),
    path('review/<int:product_id>', views.add_review,
         name='add_review'),
    path('delete_review/<int:review_id>/<int:product_id>/',
         views.delete_review, name='delete_review'),
    path('edit_review/<int:review_id>/<int:product_id>/',
         views.edit_review, name='edit_review')
]
