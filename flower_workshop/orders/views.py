from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from bouquets.models import Bouquet
from orders.models import Order
from users2.models import User2


@csrf_exempt
def create_order(request):
    global bouquet
    bouquet = request.GET
    return render(request, 'orders/order.html', context={})


@csrf_exempt
def order_step(request):
    user = User2.objects.last()
    global bouquet
    print(bouquet.get('bouquet_id'))
    bouquet_obj = Bouquet.objects.get(id=bouquet.get('bouquet_id'))
    print(request.POST)
    order = Order.objects.create(
        client=user,
        bouquet=bouquet_obj,
        price=bouquet_obj.price,
        delivery_time=request.POST.get('orderTime'),
        address=request.POST.get('adres'),
        phone=request.POST.get('tel'),
        courier=user,
        florist=user,

    )
    return render(request, 'orders/order-step.html', context={})
