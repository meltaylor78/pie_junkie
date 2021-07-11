from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q


def all_products(request):

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    roll_up = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            if 'categories|length > 1':
                roll_up = categories[0]
            print(roll_up)
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search_box' in request.GET:
            query = request.GET['search_box']
            if not query:
                messages.error(request, "No search criteria entered")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'displayed_category': categories,
        'current_sorting': current_sorting,
        'search_term': query,
        'roll_up': roll_up
    }
    return render(request, 'products/products.html', context)


def details(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/details.html', context)
