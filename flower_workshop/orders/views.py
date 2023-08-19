import re

from django.shortcuts import render

from orders.models import Order

from users2.models import User2


def order_view(request):
    if request.method == 'GET':
        user = User2.objects.last()
        time = re.findall(r'(\d+:\d+)', request.GET.get('orderTime'))
        # < QueryDict: {'fname': ['dfsds'], 'tel': ['sdffsd'], 'adres': ['sdfsdffd'], 'orderTime': ['с 12:00 до 14:00']} >
        ##TODO подставить букет и цену
        order = Order.objects.create(
            client=user,
            bouquet=...,
            price=...,
            from_delivery_time=time[0],
            to_delivery_time=time[1],
            address=request.GET.get('adres'),
            phone=request.GET.get('tel'),
            courier=user,
            florist=user,

        )

    return render(request, 'orders/order.html', context={})


def order_step(request):
    return render(request, 'orders/order-step.html', context={})
