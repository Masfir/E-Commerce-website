from django import template
from cart.models import Cart,Order

register = template.Library()

@register.filter

def cart_item_count(user):
    count_qs = Cart.objects.filter(user = user, purchase = False)
    return count_qs.count()