from django.shortcuts import render

# products view

def all_products(request):
    return render(request, 'products/products.html', context)
