from django.shortcuts import get_object_or_404, render
import stripe
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import StripeSessionIdSerializer

stripe.api_key = 'sk_test_51MaPsGBW6wAkAh0T7HTOUbYGJMEnqvj19gnpXDWSn4bjMZUbnxiVXXpB5Yg5DZmNcy3NoxVrJIxJeYXlzGqPF5M600EG9gcrAW'
PUBLIC_KEY = 'pk_test_51MaPsGBW6wAkAh0TGuRLeXVobKyekgtIZLQTqQCqi3JVk4YyjEKnrNuthG3zprHZW6XK8Lrd3TlQRbBmAWaQPmNb00tEXdL65J'

def item_detail(request, item_id): 
    template = 'item_detail.html'
    item = get_object_or_404(Item, id=item_id)
    context = {
        'item': item,
        'public_key': PUBLIC_KEY
    }
    return render(request, template, context)


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
    data = {
        'id': session.id
    }
    serializer = StripeSessionIdSerializer(data=data)
    
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)