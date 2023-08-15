from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={})


def order(request):
    return render(request, 'order.html', context={})


def catalog(request):
    return render(request, 'catalog.html', context={})


def consultation(request):
    return render(request, 'consultation.html', context={})


def card(request):
    return render(request, 'catalog.html', context={})
