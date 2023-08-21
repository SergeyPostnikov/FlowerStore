from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from bouquets.models import Bouquet
from orders.models import Order
from django.utils.timezone import localtime, timedelta


@csrf_exempt
def create_order(request):
    return render(request, 'orders/order.html')


@csrf_exempt
def order_step(request):
    bouquet = get_object_or_404(Bouquet, pk=request.POST.get('bouquet_id'))
    params = {
        'client_name': request.POST.get('client_name'),
        'bouquet': bouquet,
        'price': bouquet.price,
        'delivery_time': request.POST.get('orderTime'),
        'address': request.POST.get('adres'),
        'phone': request.POST.get('tel'),
        'paid': False,
    }
    order = Order.objects.filter(**params).last()
    if order and order.created <= localtime() - timedelta(minutes=5) or not order:
        order = Order.objects.create(**params)
    return render(
        request,
        'orders/order-step.html',
        context={
            'bouquet': bouquet,
            'order': order,
        }
    )


def my_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.paid = True
    order.save()
    bouquet = order.bouquet
    return render(
        request,
        'orders/my_order.html',
        context={
            'bouquet': bouquet,
            'order': order,
        }
    )