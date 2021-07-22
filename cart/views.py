from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    ram = None
    power = None

    if 'product_ram' in request.POST:
        ram = request.POST['product_ram']
    if 'product_power' in request.POST:
        power = request.POST['product_power']

    cart = request.session.get('cart', {})

    if ram and power:
        if item_id in list(cart.keys()):
            if ram in cart[item_id].keys() and power in cart[item_id][ram].keys():
                cart[item_id][ram][power] += quantity

            elif ram in cart[item_id].keys() and not power in cart[item_id][ram].keys():
                cart[item_id][ram][power] = quantity                           

            else:
                cart[item_id][ram]= {power: quantity}

        else:
            cart[item_id] = {ram: {power: quantity}}
    
        messages.success(request, f'{product.name} (with {ram} Ram & {power} plug) added to cart')
   
    elif ram and not power:
        if item_id in list(cart.keys()):
            if ram in cart[item_id]['product_ram'].keys():
                cart[item_id]['product_ram'][ram] += quantity
            else:
                cart[item_id]['product_ram'][ram] = quantity
        else:
            cart[item_id] = {'product_ram': {ram: quantity}}

        messages.success(request, f'{product.name} (with {ram} Ram) added to cart')

    elif power and not ram:
        if item_id in list(cart.keys()):
            if power in cart[item_id]['product_power'].keys():
                cart[item_id]['product_power'][power] += quantity
            else:
                cart[item_id]['product_power'][power] = quantity
        else:
            cart[item_id] = {'product_power': {power: quantity}}

        messages.success(request, f'{product.name} (with {power} plug) added to cart')

    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity
        print(f'Added {product.name} to shopping cart')
        
        messages.success(request, f'{product.name} to cart')

    request.session['cart'] = cart
    return redirect(redirect_url)

def update_cart(request, item_id):
    quantity = int(request.POST.get('quantity'))
    ram = None
    power = None

    if 'product_ram' in request.POST:
        ram = request.POST['product_ram']

    if 'product_power' in request.POST:
        power = request.POST['product_power']

    cart = request.session.get('cart', {})

    if ram and power:
        if quantity > 0:
            cart[item_id][ram][power] = quantity
        else:
            del cart[item_id][ram][power]
            if not cart[item_id][ram]:
                del cart[item_id][ram]
            if not cart[item_id]:
                cart.pop(item_id)
   
    elif ram and not power:
        if quantity > 0:
            cart[item_id]['product_ram'][ram] = quantity
        else:
            del cart[item_id]['product_ram'][ram]
            if not cart[item_id]['product_ram']:
                cart.pop(item_id)

    elif power and not ram:
        if quantity > 0:
            cart[item_id]['product_power'][power] = quantity
        else:
            del cart[item_id]['product_power'][power]
            if not cart[item_id]['product_power']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_item(request, item_id):
    try:
        ram = None
        power = None

        if 'product_ram' in request.POST:
            ram = request.POST['product_ram']

        if 'product_power' in request.POST:
            power = request.POST['product_power']

        cart = request.session.get('cart', {})
        if ram and power:
            del cart[item_id][ram][power]
            if not cart[item_id][ram]:
                del cart[item_id][ram]
            if not cart[item_id]:
                cart.pop(item_id)
    
        elif ram and not power:
            del cart[item_id]['product_ram'][ram]
            if not cart[item_id]['product_ram']:
                cart.pop(item_id)

        elif power and not ram:
            del cart[item_id]['product_power'][power]
            if not cart[item_id]['product_power']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

