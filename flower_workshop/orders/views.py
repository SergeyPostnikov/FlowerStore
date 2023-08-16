from django.shortcuts import render

from flower_workshop.orders.models import Order


def order(request):

    return render(request, 'orders/order.html', context={})


def order_step(request):
    return render(request, 'orders/order-step.html', context={})
