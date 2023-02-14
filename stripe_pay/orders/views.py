import os

import stripe
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Item
from .serializers import StripeSessionIdSerializer

import socket


load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY', default='default')
PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', default='default')
CURRENCY = 'rub'
QUANTITY = 1
MODE = 'payment'


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
    host = request.get_host()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    sok = s.getsockname()[0]
    s.close()
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': CURRENCY,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': QUANTITY,
        }],
        mode=MODE,
        success_url='http://' + sok + reverse('orders:success'),
        cancel_url='http://' + sok + reverse('orders:cancel'),
    )
    data = {
        'id': session.id
    }
    serializer = StripeSessionIdSerializer(data=data)

    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'