from cart.models import Cart

def cart_item_count(request):
    u = request.user
    total = 0
    if u.is_authenticated:
        cart = Cart.objects.filter(user=u)
        for item in cart:
            total += item.quantity
    else:
        total = 0        
    return {'items': total}