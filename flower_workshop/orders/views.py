import re

from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from bouquets.models import Bouquet
from orders.models import Order
from users2.models import User2


def order_view(request):
    if request.method == 'GET':
        user = User2.objects.last()
        bouquet_id = request.GET.get('bouquet_id')
        print(bouquet_id)
        if bouquet_id:
            bouquet = get_object_or_404(Bouquet, pk=bouquet_id)
            # time = re.findall(r'(\d+:\d+)', request.GET.get('orderTime'))
            # < QueryDict: {'fname': ['dfsds'], 'tel': ['sdffsd'], 'adres': ['sdfsdffd'], 'orderTime': ['с 12:00 до 14:00']} >
            ##TODO подставить букет и цену
            # order = Order.objects.create(
            #     client=user,
            #     bouquet=...,
            #     price=...,
            #     # from_delivery_time=time[0],
            #     # to_delivery_time=time[1],
            #     address=request.GET.get('adres'),
            #     phone=request.GET.get('tel'),
            #     courier=user,
            #     florist=user,
            #
            # )
            context = {
                'bouquet': bouquet,
            }
            return render(request, 'orders/order.html', context)
        raise Http404


def order_step(request):
    return render(request, 'orders/order-step.html', context={})
