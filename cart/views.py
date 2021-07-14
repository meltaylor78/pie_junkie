from django.shortcuts import render, redirect

def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    ram = None
    power = None

    if 'product_ram' in request.POST:
        ram = request.POST['product_ram']
   
    if 'product_power' in request.POST:
        power = request.POST['product_power']

    cart = request.session.get('cart', {})

    if ram:
        if item_id in list(cart.keys()):
            if ram in cart[item_id]['ram_size'].keys():
                cart[item_id]['ram_size'][ram] += quantity
                print ("This")
                print (cart[item_id]['ram_size'][ram])
            else:
                cart[item_id]['ram_size'][ram] = quantity
        else:
            cart[item_id] = {'ram_size': {ram: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)