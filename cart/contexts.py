from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from products.models import Product


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            sub_total = item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'sub_total': sub_total
            })

        elif 'product_ram' not in item_data.keys():
            product = get_object_or_404(Product, pk=item_id)
            ram_options = list(item_data.keys())
            for opt in ram_options:
                for power, quantity in item_data[opt].items():
                    total += quantity * product.price
                    sub_total = quantity * product.price
                    product_count += quantity
                    cart_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'ram': opt,
                        'power': power,
                        'sub_total': sub_total
                    })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for ram, quantity in item_data['product_ram'].items():
                total += quantity * product.price
                sub_total = quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'ram': ram,
                    'sub_total': sub_total
                })

    if total < settings.FREE_DELIVERY:
        delivery = total * Decimal(settings.DELIVERY_PERCENT / 100)
        free_delivery_delta = settings.FREE_DELIVERY - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.DELIVERY_PERCENT,
        'grand_total': grand_total,
    }

    return context
