from django.shortcuts import render, redirect
from mainapp.models import Product
from .models import CartItem


# to redirect to login page when required
from django.contrib.auth.decorators import login_required


# implementing AJAX to update cart item quantity without refresh
from django.http import JsonResponse   #its not http response
from django.shortcuts import get_object_or_404


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


    return redirect('view_cart')  # redirect- they are handel html request directly, javascript accept response but in class view html accept response
    

# R - Read CartItem

def viewCart(request):
    template = 'cart.html'
    cart_item = CartItem.objects.filter(user = request.user)  # filter will multiple object
    # the above statement is equivalent to : SELECT * FROM cartitem WHERE user = <USER_ID>;
    total_price = sum(float(item.product.price) * item.quantity for item in cart_item)

    context = {
        'cart_items' : cart_item,
        'total_price' : total_price
    }

    return render(request, template, context)


# Deleteing(removing) order from cart item 

def removeFromCart(request, cart_item_id):
    this_cart_item = CartItem.objects.get(id = cart_item_id)  # get mens single object only
    this_cart_item.delete()  # deletes the associate record as well as the cartitem obj in memory

    return redirect('view_cart')

# function based views for implementing the API endpoints for cart quantity updations
# its not http response, it's a JOSM responce
# below mention addquntity and remquntity use for + and - button for editing quntity only
@login_required
def addQuantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    overall_total = sum(item.get_total_price() for item in CartItem.objects.filter(user=request.user))
    return JsonResponse({'quantity': cart_item.quantity, 'total_price': cart_item.get_total_price(), 'overall_total': overall_total})

@login_required
def remQuantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        overall_total = sum(item.get_total_price() for item in CartItem.objects.filter(user=request.user))
        return JsonResponse({'quantity': cart_item.quantity, 'total_price': cart_item.get_total_price(), 'overall_total': overall_total})
    else:
        cart_item.delete()
        overall_total = sum(item.get_total_price() for item in CartItem.objects.filter(user=request.user))
        return JsonResponse({'quantity': 0, 'total_price': 0, 'overall_total': overall_total})