from django.shortcuts import render


def order(request):
    return render(request, 'orders/order.html', context={})


def order_step(request):
    return render(request, 'orders/order-step.html', context={})
