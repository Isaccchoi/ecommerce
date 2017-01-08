from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.

from products.models import Variation
from carts.models import Cart
from carts.models import CartItem

class CartView(View):
    def get(self, request, *args, **kwargs):
        request.session.set_expiry(600) # 10 minutes
        cart_id = request.session.get("cart_id")
        if cart_id == None:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
        if request.user.is_authenticated():
            cart.user = request.user
            cart.save()
        item_id = request.GET.get("item")
        delete_item = request.GET.get("delete")
        if item_id:
            item_instance = get_object_or_404(Variation, id=item_id)
            qty = request.GET.get("qty")
            cart_item, _ = CartItem.objects.get_or_create(cart=cart, item=item_instance)
            if delete_item:
                cart_item.delete()
            else:
                cart_item.quantity = qty
                cart_item.save()
        return HttpResponseRedirect("/")
