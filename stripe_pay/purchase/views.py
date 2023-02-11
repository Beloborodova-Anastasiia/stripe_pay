from django.shortcuts import get_object_or_404, redirect, render
import stripe
from rest_framework.decorators import api_view  
from rest_framework.response import Response

from .models import Item

stripe.api_key = 'sk_test_26PHem9AhJZvU623DfE1x4sd'


@api_view(['GET',])  
def item_detail(request, item_id): 
    template = 'item_detail.html'
    item = get_object_or_404(Item, id=item_id)
    context = {
        'item': item,
        'redirect_path': f'/buy/{item_id}'
    }
    return render(request, template, context)



# def item_checkout(request, item_id):
#     template = 'item_detail.html'
#     item = get_object_or_404(Item, id=item_id)
#     context = {
#         'item': item,
#         'redirect_path': f'/buy/{item_id}'
#     }
#     print('!!!!!!!!!!!!!!!!!!!')
#     return render(request, template, context)


@api_view(['GET',])  
def create_checkout_session(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel',
    )
    print(session.id)

    return redirect(session.url, code=303)