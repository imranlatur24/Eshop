from django import template

register=template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    print(keys)
    cart_keys=list(keys)
    for id in keys:
        print('card id ',id)
        if int(id) == product.id:
            return True
    return False;   

@register.filter(name='cart_count_quantity')
def cart_count_quantity(product,cart):
    keys=cart.keys()
    print(keys)
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;   

@register.filter(name='price_total')
def price_total(product,cart):
    return int(product.price) * int(cart_count_quantity(product,cart))

# @register.filter(name='total_cart_price')
# def total_cart_price(products,cart):
#     print('products ',products) 
#     print('products type ',type(products))

#     sum=0
#     for p in products:
#         sum += total_cart_price(p,cart)
#     return sum
