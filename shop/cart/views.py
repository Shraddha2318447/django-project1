from django.shortcuts import render, redirect
from mainapp.models import Product
from .models import CartItem

from django.contrib.auth.decorators import login_required
# Create your views here.
# c- Creating cart items


@login_required
def addToCart(request, product_id):
    this_product = Product.objects.get(id = product_id)  # fetching the product object
    # When adding product to cart, we need to check if the same user havs added the same product to cart before, in that case,  we will not craete a new cart item, rather just increase quntity
    

    cart_item, created = CartItem.objects.get_or_create(product = this_product, user = request.user)
    cart_item.quantity += 1
    # Above two statements are equivalent to 'INSERT into table ... on duplicate key upadate .....'
    cart_item.save()  # save changes to SQL through update


    return redirect('view_cart')


# R - Read CartItem

def viewCart(request):
    template = 'cart.html'
    cart_item = CartItem.objects.filter(user = request.user)
    # the above statement is equivalent to : SELECT * FROM cartitem WHERE user = <USER_ID>;
    total_price = sum(float(item.product.price) * item.quantity for item in cart_item)

    context = {
        'cart_items' : cart_item,
        'total_price' : total_price
    }

    return render(request, template, context)
