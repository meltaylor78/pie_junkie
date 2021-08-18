from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Cust_Review
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .forms import ProductForm, AddReviewForm
from django.contrib.auth.models import User


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
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search_box' in request.GET:
            query = request.GET['search_box']
            if not query:
                messages.warning(request,
                                 'No search criteria entered')

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
    cust_reviews = Cust_Review.objects.filter(
        product=product).order_by('-date')

    context = {
        'product': product,
        'cust_reviews': cust_reviews
    }

    return render(request, 'products/details.html', context)


@login_required
def add_review(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        user_product = Cust_Review(user=request.user, product=product)
        form = AddReviewForm(request.POST, instance=user_product)

        if form.is_valid():
            form.save()
            messages.info(request, "Your review has been posted")
        else:
            messages.error(request, ("Error saving review," +
                           "please try again later"))
    else:
        messages.error(request, "You must be logged in to post a review")
    return redirect("details", product_id=product_id)


def edit_review(request, review_id, product_id):
    review = get_object_or_404(Cust_Review, id=review_id)
    user = get_object_or_404(User, id=review.user.id)

    if request.user.is_authenticated:
        if request.user == user:
            if request.method == "GET":
                form = AddReviewForm(instance=review)
                context = {
                    "form": form,
                    "product_id": product_id,
                }

                return render(request, "products/edit_review.html", context)
            elif request.method == "POST":
                review_edit = AddReviewForm(request.POST, instance=review)
                if review_edit.is_valid():
                    review_edit.save()
                    messages.info(request,
                                  "Edited review has been posted")
                    return redirect("details", product_id=product_id)
                else:
                    messages.error(
                        request, "Error editing review, try again later")
                    return redirect("details", product_id=product_id)
        else:
            messages.error(request, "Requested action not allowed")
            return redirect("details", product_id=product_id)

    else:
        messages.error(request, "Requested action not allowed")
        return redirect("details", product_id=product_id)


@login_required
def delete_review(request, review_id, product_id):
    review = get_object_or_404(Cust_Review, id=review_id)
    user = get_object_or_404(User, id=review.user.id)

    if request.user.is_authenticated:
        if request.user == user:
            review_to_delete = get_object_or_404(Cust_Review, id=review_id)
            review_to_delete.delete()

            messages.info(request,
                          'Product review has been posted')

            return redirect("details", product_id=product_id)

        else:
            messages.error(request, "Requested action not allowed")
            return redirect("details", product_id=product_id)

    else:
        messages.error(request, "Requested action not allowed")
        return redirect("details", product_id=product_id)


@login_required
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save()

            messages.info(request,
                          'New Product has been added.')

            return redirect(reverse('details', args=[product.id]))
        else:
            messages.error(request,
                           'Add new product failed, \
                           please recheck the form is valid.')

    else:
        form = ProductForm()

    template = 'products/new_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:

        messages.error(request,
                       'You must be am admin to delete a product')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()

    messages.info(request,
                  'The product has been deleted from the DB.')

    return redirect(reverse('products'))


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request,
                       'You must be am admin to edit product details')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updates habe been savd')
            return redirect(reverse('details', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update product, \
                               please recheck the form is valid.')

    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
