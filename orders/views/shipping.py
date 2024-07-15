from django.shortcuts import render,redirect
from orders.forms import *

def create_shipping(request):
    return render(request, 'shipping/create_shipping.html')

def shipping_items(request):
    form = ShippingItemForm.objects.all()

    context={
        'form': form
    }

    return render(request,'shipping/create_shipping_item.html', context)